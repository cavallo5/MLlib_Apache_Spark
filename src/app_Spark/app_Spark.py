from pyspark import SparkContext, SparkConf

# Creazione SparkContext
conf = SparkConf().setAppName('Spark')
sc = SparkContext(conf=conf)

# Creazione dataset

datasetRDD = sc.textFile("file:////hpc/home/vincenzo.cavallo/myspark/spark-2.4.0-bin-hadoop2.7/test_mllib/app_Spark/u.user")

# Funzione che effettua lo split() e richiama la funzione divisione_eta() per restituire i valori da salvare nel RDD
def fascia_eta(data):
             userid,age,gender,occupation,zip = data.split("|")
             return  userid, divisione_eta(int(age)),gender,occupation,zip,int(age)

# Funzione che effettua una divisione in fasce d'eta' degli utenti sulla base del parametro age passato
def  divisione_eta(age):
        if age < 10 :
           return '0-10'
        elif age < 20:
           return '10-20'
        elif age < 30:
           return '20-30'
        elif age < 40:
           return '30-40'
        elif age < 50:
           return '40-50'
        elif age < 60:
           return '50-60'
        elif age < 70:
           return '60-70'
        elif age < 80:
           return '70-80'
        else :
           return '80+'

# Creazione RDD dal datasetRDD in cui applico la funzione fascia_eta ad ogni riga tramite map()
datasetRDD_gruppi_eta = datasetRDD.map(fascia_eta)
# Creazione RDD tramite trasformazione filter() 
datasetRDD_20_30 = datasetRDD_gruppi_eta.filter(lambda line : '20-30' in line)
# datasetRDD_20_30 contiene le sole stringhe degli utenti che fanno parte della fascia d'eta' 20-30

print "persone totali: ",datasetRDD.count()
print "persone 20-30 ",datasetRDD_20_30.count()
