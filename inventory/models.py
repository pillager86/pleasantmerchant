from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy

class Item(models.Model):
    class Department(models.TextChoices):
        DAIRY = "DAI", gettext_lazy('Dairy')
        FROZEN = "FRO", gettext_lazy('Frozen')
        GROCERY = "GRO", gettext_lazy('Grocery')
    
    upc = models.CharField(max_length=11, 
        validators=[MinLengthValidator(11, "10 digit UPC must have leading 0")],
        primary_key=True)
    name = models.CharField(max_length=50)
    case_qty = models.IntegerField()
    case_cost = models.DecimalField(decimal_places=2, max_digits=6)
    full_price = models.DecimalField(decimal_places=2, max_digits=6)
    member_price = models.DecimalField(decimal_places=2, max_digits=6)
    department = models.CharField(max_length=3, choices=Department.choices, default=Department.DAIRY)
    qoh = models.IntegerField(default=0)

    def __str__(self):
        return self.upc + " " + self.name + " (" + self.get_department_display() + ")"

