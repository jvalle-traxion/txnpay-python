from traxionpay.traxionpay_client import TraxionPay

api = TraxionPay(secret_key="cxl+hwc%97h6+4#lx1au*ut=ml+=!fx85w94iuf*06=rf383xs", api_key="7)5dmcfy^dp*9bdrcfcm$k-n=p7b!x(t)_f^i8mxl@v_+rno*x")


site_url = "https://dev.traxionpay.com/"
api_url = "https://devapi.traxionpay.com/"

api.cash_in(
            merchant_id=6328,
            merchant_ref_no="ABC123DEF456",
            merchant_additional_data="",
            description="Test description",
            amount=1500,
            billing_email="sample@email.com",
            billing_first_name="John",
            billing_last_name="Doe",
            billing_middle_name="Peters",
            billing_mobile="09123456789",
            billing_address="Sampalok St. Emerald Village",
            billing_zip="8000",
            billing_country="PH",
            status_notification_url='{}callback'.format(api_url),
            success_page_url='{}'.format(site_url),
            failure_page_url='{}'.format(site_url),
            cancel_page_url='{}'.format(site_url),
            pending_page_url='{}'.format(site_url))