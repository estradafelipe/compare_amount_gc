# Load libraries
import pandas as pd


# Load dataset
#Defino las columnas
names1 = ['MerchantID', 'ContractID',  'OrderID', 'EffortID',  'MerchantReference',
     'PaymentReference',  'CustomerID', 'StatusID', 'StatusDescription', 'PaymentProduct ID',
     'PaymentProductDescription',  'OrderCountryCode', 'OrderCurrencyCode',  'OrderAmount',
     'RequestCurrencyCode',  'RequestAmount', 'PaidCurrency',  'PaidAmount',  'ReceivedDate',
     'StatusDate',  'RejectionCode', 'Remarks']
#Cargo el archivo
globalcollect = pd.read_csv(r'C:\Users\feliestrada\Desktop\Python\Sodimac\amount_dif\report_gc_may.csv',
                        header=0 , names=names1, encoding='latin-1', index_col=False, low_memory=False)

#Defino las columnas
names2 = ['CANAL','OC','MONTO','GC_ORDER','FECHA']
#Cargo el archivo
asl = pd.read_csv(r'C:\Users\feliestrada\Desktop\Python\Sodimac\amount_dif\cabecera_asl2.csv', delimiter=',',
                header=0, names=names2, low_memory=False)

print("Globalcollect:")
# shape
print(globalcollect.shape)
# head
#print(globalcollect.head(20))

print("ASL: ")
# shape
print(asl.shape)

#print(agrupado_asl.head(20))
print(asl.head(20))

gc_tr = globalcollect[globalcollect.EffortID.isin(['1'])]

asl_gc_merge = asl.merge(gc_tr[['OrderID','StatusID','OrderAmount','RequestAmount']],
                                left_on='GC_ORDER' ,right_on='OrderID', how='left')

asl_gc_merge['compare_amount'] = asl_gc_merge['MONTO'] == asl_gc_merge['OrderAmount']
asl_gc_merge = asl_gc_merge.dropna()
print(asl_gc_merge.head(20))
asl_gc_merge.to_csv("asl_gc_merge.csv",index=False)
