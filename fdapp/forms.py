from django import forms
from .models import FixedDeposit
from datetime import datetime

def get_financial_years():
    current_year = datetime.now().year
    start_year = current_year if datetime.now().month >= 4 else current_year - 1
    return [f"FY {y}-{str(y+1)[-2:]}" for y in range(start_year, start_year + 16)]

class FixedDepositForm(forms.ModelForm):
    financial_year = forms.ChoiceField(
        choices=[(fy, fy) for fy in get_financial_years()],
        widget=forms.Select(attrs={'class': 'form-select'}),
        initial=f"FY {datetime.now().year}-{str(datetime.now().year + 1)[-2:]}"
        if datetime.now().month >= 4
        else f"FY {datetime.now().year - 1}-{str(datetime.now().year)[-2:]}"
    )

    class Meta:
        model = FixedDeposit
        fields = [
            'customer_id', 'fd_number', 'bank_name',
            'principal', 'rate', 'financial_year',
            'start_date', 'maturity_date', 'accumulation'
        ]
        widgets = {
            'customer_id': forms.TextInput(attrs={'class': 'form-control'}),
            'fd_number': forms.TextInput(attrs={'class': 'form-control'}),
            'bank_name': forms.Select(attrs={'class': 'form-select'}),  # ✅ dropdown
            'principal': forms.NumberInput(attrs={'class': 'form-control'}),
            'rate': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'maturity_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'accumulation': forms.Select(attrs={'class': 'form-select'}),  # ✅ dropdown
        }
