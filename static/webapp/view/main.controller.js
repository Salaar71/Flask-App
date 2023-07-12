sap.ui.define(
[ "sap/ui/core/mvc/Controller", "sap/m/MessageToast", 'sap/m/Button', 'sap/m/Dialog', 'sap/m/Text', 'sap/m/MessageBox', "sap/ui/model/json/JSONModel", "sap/m/BusyDialog", "sap/ui/core/Fragment" ], 
function(Controller, MessageToast, Button, Dialog, Text, MessageBox, JSONModel, BusyDialog, Fragment)
{
	"use strict";

	return Controller.extend("webapp.view.main",
	{
		
		currentUserInfo : "",
		onInit : function()
		{
			debugger;
			var that = this;
			$.sap.isAuthUser = false;
			sap.ui.core.BusyIndicator.show();
			$.ajax(
			{
				cache : false,
				type : "GET",
				url : "../../employees"
			}).success(function(empList)
			{
				debugger;
				
				var empModel = new JSONModel(empList);
				that.getView().setModel(empModel, "empModel1");
				debugger;
				MessageBox.success("API call completed successfully");
				
				sap.ui.core.BusyIndicator.hide();
			}).fail(function(jqXHR, exception)
			{
				debugger;
				sap.ui.core.BusyIndicator.hide();
				MessageBox.error("Error, please re-check");
			});

		},

	
	});

});