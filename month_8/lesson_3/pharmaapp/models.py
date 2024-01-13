from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=30, verbose_name='Ism')
    l_name = models.CharField(max_length=30, verbose_name='Familiya')
    gender = models.CharField(max_length=10,verbose_name='Jins')
    age = models.IntegerField(verbose_name='Yosh')
    contact_add = models.IntegerField(verbose_name='Nomer')
    cust_email = models.EmailField(verbose_name='Email')
    cust_pass = models.CharField(max_length=50,verbose_name='Pass')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Customer table '
        verbose_name_plural = 'Customer tables '

class Pharmacist(models.Model):
    name = models.CharField(max_length=30, verbose_name='Ism')
    l_name = models.CharField(max_length=30, verbose_name='Familiya')
    gender = models.CharField(max_length=10,verbose_name='Jins')
    age = models.IntegerField(verbose_name='Yosh')
    contact_add = models.IntegerField(verbose_name='Nomer')
    admin_email = models.EmailField(verbose_name='Email')
    admin_pass = models.CharField(max_length=50, verbose_name='Pass')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Pharmacist table '
        verbose_name_plural = 'Pharmacist tables '


class Medicines(models.Model):
    MED_CATEGORY = (
        ('kapsula', 'Kapsula shaklda'),
        ('qattiq', 'Qattiq shaklda'),
        ('kukun', 'Kukun shaklda'),
        ('suyuq', 'Suyuq shaklda'),
        )
    med_category = models.CharField(max_length=20, choices=MED_CATEGORY, default='qattiq shaklda', verbose_name='Kategoriya')
    name = models.CharField(max_length=30, verbose_name='Nomi')
    description = models.TextField(verbose_name='Haqida')
    price = models.IntegerField(verbose_name='Narxi')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Medicines table '
        verbose_name_plural = 'Medicines tables '


class Purchasing(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    med_id = models.ForeignKey(Medicines, on_delete=models.CASCADE)
    amount = models.IntegerField(verbose_name='Soni')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Sotilgan kun')

    def __str__(self):
        return str(self.med_id)

    class Meta:
        verbose_name = 'Purchasing table '
        verbose_name_plural = 'Purchasing tables '


class Sales(models.Model):
    pharm_id = models.ForeignKey(Pharmacist, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    med_id = models.ForeignKey(Medicines, on_delete=models.CASCADE)
    count = models.IntegerField(verbose_name='Soni')
    purchase_id = models.ForeignKey(Purchasing, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    total_amount = models.IntegerField(verbose_name='Sotilgan maxsulot soni')
    
    def __str__(self):
        return str(self.pharm_id)
    
    class Meta:
        verbose_name = 'Sales table '
        verbose_name_plural = 'Sales tables '

class Reports(models.Model):
    purchase_id = models.ForeignKey(Purchasing, on_delete=models.CASCADE)
    sales_id = models.ForeignKey(Sales, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Sotilgan kun')
    
    def __str__(self):
        return str(self.sales_id)
    
    class Meta:
        verbose_name = 'Reports table '
        verbose_name_plural = 'Reports tables '