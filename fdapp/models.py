from django.db import models

# ✅ Bank Choices
BANK_CHOICES = [
    ('HDFC', 'HDFC Bank'),
    ('SBM', 'State Bank Mauritius'),
    ('YES', 'Yes Bank'),
    ('IDFC', 'IDFC Bank'),
    ('ICICI', 'ICICI Bank'),
    ('AXIS', 'Axis Bank'),
    ('BOB', 'Bank of Baroda'),
    # Tumhi ithe ajun banks add karu shakta
]

class FixedDeposit(models.Model):
    # ✅ Basic FD Info
    customer_id = models.CharField(max_length=100)
    fd_number = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=100, choices=BANK_CHOICES)
    principal = models.IntegerField()
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    maturity_date = models.DateField()

    # ✅ Additional Fields
    financial_year = models.CharField(max_length=10, blank=True, null=True)

    # ✅ Calculation Fields
    interest = models.FloatField(blank=True, null=True)          # Total calculated interest
    tds = models.FloatField(blank=True, null=True)               # TDS on interest
    closing_balance = models.FloatField(blank=True, null=True)   # Final FD value
    interest_type = models.CharField(                            # 'Accrued' or 'Actual'
        max_length=20, blank=True, null=True
    )
    accumulation = models.CharField(                             # 'Yes' or 'No'
        max_length=3,
        choices=[('Yes', 'Yes'), ('No', 'No')],
        default='Yes'
    )

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_id} - {self.fd_number}  ₹{self.principal} @ {self.rate}%"
