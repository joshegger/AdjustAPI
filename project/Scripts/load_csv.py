import csv
from models import Metrics


def import_csv():
    with open('dataset.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            print(row)
            Metrics(
                date=row[0],
                channel=row[1],
                country=row[2],
                os=row[3],
                impressions=int(row[4]),
                clicks=int(row[5]),
                installs=int(row[6]),
                spend=float(row[7]),
                revenue=float(row[8])
                ).save()
    return Metrics

if __name__ == '__main__':
    Metrics.objects.bulk_create(import_csv())
    print(Metrics.objects.all().count())