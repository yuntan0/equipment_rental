# Copyright (c) 2025, John and contributors
# For license information, please see license.txt

import frappe , json ,requests
from frappe import _
from frappe.model.document import Document


class VehicleMaster(Document):
    def validate(self):
        pass
    
    def before_save(self):
        if self.model  and self.plate and self.model_year:
            self.title = self.model + " " + self.plate + " " + self.model_year
        
    @frappe.whitelist()
    def get_vin_api(self):
        # self.validate_values()
        url = "https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVINValuesBatch/"

        payload = "DATA=" + self.vin_number + "&format=JSON"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        response = requests.request("POST", url, headers=headers, data=payload)
        if response.status_code == 200:
            # print(response.text)
            res = json.loads(response.content)
            if res.get("Count") > 0:
                # print(res.get("Results")[0].get("VehicleType"),res.get("Results")[0].get("Make"),res.get("Results")[0].get("Manufacturer"),res.get("Results")[0].get("Model"),res.get("Results")[0].get("ModelYear"))
                self.model_year = res.get("Results")[0].get("ModelYear")
                self.model = res.get("Results")[0].get("Model")
                self.maker = res.get("Results")[0].get("Make")
                self.manufacturer = res.get("Results")[0].get("Manufacturer")
                self.model = res.get("Results")[0].get("Model")
                self.vehicle_type = res.get("Results")[0].get("VehicleType")
                print(response.text)
                # self.vin_lookup_json = response.text
                frappe.msgprint(
                    _(" {0} ").format(res.get("Results")[0].get("ErrorText"))
                )
                self.save()
                # self.dbas = res.get("Results")[0].get("Model")
            # elif res.get("Count")==0:
            #     frappe.throw(_("Vin number is not valid {0} ").format(self.serial_no))

        # self.save()
        # a =  np.npv(0.281,[-100, 19, 49, 58, 200])
	