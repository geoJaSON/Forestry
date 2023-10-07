function loadContract() {
    console.log(sale)
    //populate fields based on sale
    document.getElementById('ContractTitle').value = sale.attributes.ContractTitle;
    document.getElementById('ContractID').value = sale.attributes.ContractID;
    document.getElementById('InvitationID').value = sale.attributes.ContractType;
    document.getElementById('militaryorcivilcode').value = sale.attributes.militaryorcivilcode;
    document.getElementById('PrimarySpecies').value = sale.attributes.PrimarySpecies;
    document.getElementById('LoggingStartDate').value = formatUnixTimestamp(sale.attributes.LoggingStartDate);
    document.getElementById('LoggingEndDate').value = formatUnixTimestamp(sale.attributes.LoggingEndDate);
    document.getElementById('installation').value = sale.attributes.installation;
    document.getElementById('TrainingArea').value = sale.attributes.TrainingArea;
    document.getElementById('county').value = sale.attributes.county;
    document.getElementById('TownshipRangeSection').value = sale.attributes.TownshipRangeSection;
    document.getElementById('Latitude').value = sale.attributes.Latitude;
    document.getElementById('Longitude').value = sale.attributes.Longitude;
    document.getElementById('grid').value = sale.attributes.grid;
    document.getElementById('ContractType').value = sale.attributes.ContractType;
    document.getElementById('SalesContractStatus').value = sale.attributes.SalesContractStatus;
    //document.getElementByName('Declared_Supplemental').value = sale.attributes.Declared_Supplemental;
    document.getElementById('TimberSalesSpecialist').value = sale.attributes.TimberSalesSpecialist;
    document.getElementById('purchaser').value = sale.attributes.purchaser;
    document.getElementById('PurchaserPOCPhone').value = sale.attributes.PurchaserPOCPhone;
    document.getElementById('PurchaserPOC').value = sale.attributes.PurchaserPOC;
    document.getElementById('PurchaserPOCEmail').value = sale.attributes.PurchaserPOCEmail;
    document.getElementById('logger').value = sale.attributes.logger;
    //document.getElementById('UnitOfMeasurement').value = sale.attributes.UnitOfMeasurement;
    document.getElementById('ContractAcres').value = sale.attributes.ContractAcres;


    const purchaserSelect = document.getElementById('purchaser');
    const loggerSelect = document.getElementById('logger');

    purchaserSelect.innerHTML = '';
    loggerSelect.innerHTML = '';
    console.log(contacts)
    const sortedFeatures = contacts.sort((a, b) => {
        if (a.attributes.ContactBusinessName < b.attributes.ContactBusinessName) return -1;
        if (a.attributes.ContactBusinessName > b.attributes.ContactBusinessName) return 1;
        return 0;
    });




}

