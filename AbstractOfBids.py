#%%
import requests, arcpy, datetime
import pandas as pd

from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.generic import BooleanObject, NameObject, IndirectObject

contract = arcpy.GetParameterAsText(0)
#contract = '10-100'
#%%
response = requests.get(f'https://arcportal-ucop-corps.usace.army.mil/s0arcgis/rest/services/Hosted/NWS_Forestry_Database/FeatureServer/0/query?where=contractid=%27{contract}%27&outFields=*&returnGeometry=false&f=json')
sale = response.json()['features'][0]['attributes']
pgid = sale['globalid']
response = requests.get(f'https://arcportal-ucop-corps.usace.army.mil/s0arcgis/rest/services/Hosted/NWS_Forestry_Database/FeatureServer/8/query?where=parentglobalid=%27{pgid}%27&outFields=*&returnGeometry=false&f=json')
bids_df = pd.DataFrame(response.json()["features"])
#%%
def set_need_appearances_writer(writer: PdfFileWriter):
    try:
        catalog = writer._root_object
        if "/AcroForm" not in catalog:
            writer._root_object.update({
                NameObject("/AcroForm"): IndirectObject(len(writer._objects), 0, writer)
            })

        need_appearances = NameObject("/NeedAppearances")
        writer._root_object["/AcroForm"][need_appearances] = BooleanObject(True)
        return writer

    except Exception as e:
        print('set_need_appearances_writer() catch : ', repr(e))
        return writer
    
# %%
infile = r"C:\Users\g3retjjj\Downloads\Abstract_of_Bids.pdf"
f = open(infile, "rb")
pdf = PdfFileReader(f, strict=False)

update_dict = {'Timber Sale Name': sale['contracttitle'],
               'Invitation No': sale['invitationid'],
               'Bid Opening Date': datetime.datetime.fromtimestamp(sale['invitationdate']/1000).strftime('%m-%d-%Y'),
               'Legal Description': sale['townshiprangesection'],
               'Contract No': sale['contractid'],
               'Product': sale['primaryspecies'].replace('_',' '),
               'Volume': '',
               'Min Bid': '',
               'Name and Title':sale['abstractpocname']+'\n'+sale['abstractpoctitle'],}

for index, row in bids_df.iterrows():
    update_dict['BIDDER NAME AND ADDRESS'+str(index+1)] = row['attributes']['biddername']+'\n'+row['attributes']['bidderaddress']
    update_dict[str(index+1)] = row['attributes']['abstractunitbid']
    update_dict[str(index+1)+'_'+str(index+1)] = ''
    update_dict["BID DIPOSIT"+str(index+1)] =row['attributes']['abstractbiddeposit']

page = pdf.getPage(0)
writer = PdfFileWriter()
set_need_appearances_writer(writer)
writer.updatePageFormFieldValues(page, fields=update_dict)
writer.addPage(page)
outfile = arcpy.GetParameterAsText(1)
with open(outfile, "wb") as fh:
    writer.write(fh)