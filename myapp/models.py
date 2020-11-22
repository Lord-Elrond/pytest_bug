from django.db import models, connection


class ValManager(models.Manager):
    def pivot(self):
        sql = """
        SELECT * FROM
        crosstab($$
          SELECT product_id, attr_id, label
          FROM myapp_val
          ORDER BY 1
        $$, $$
          VALUES ('make'), ('color')
        $$) AS ct(
          "product_id" integer,
          "rarity" text,
          "color" text
        ) WHERE product_id IN (1, 2)
        """
        columns = ['product_id', 'rarity', 'color']
        with connection.cursor() as cursor:
            cursor.execute(sql)
            return [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]

class Product(models.Model):
    pass

class Attr(models.Model):
    id = models.CharField(max_length=45, primary_key=True)

class Val(models.Model):
    attr = models.ForeignKey(Attr, on_delete=models.CASCADE)
    label = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    objects = ValManager()
