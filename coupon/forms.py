from django import forms


class AddCouponForm(forms.Form):
    code = forms.CharField(label='쿠폰 등록하기')