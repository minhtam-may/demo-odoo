import { models } from "@web/../tests/web_test_helpers";

export class CrmLead extends models.ServerModel {
    _name = "crm.lead";
    _views = {
        form: /* xml */ `
            <form string="Lead">
                <sheet>
                    <field name="name"/>
                </sheet>
            </form>`,
    };
}
