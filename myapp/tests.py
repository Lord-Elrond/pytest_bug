import pytest

from .models import Product, Attr, Val

pytestmark = pytest.mark.django_db


@pytest.fixture
def products():
    p1 = Product.objects.create()
    p2 = Product.objects.create()
    return p1, p2

@pytest.fixture
def attrs():
    attr1 = Attr.objects.create(id='make')
    attr2 = Attr.objects.create(id='color')
    return attr1, attr2

@pytest.fixture
def vals(products, attrs):
    p1, p2 = products
    attr1, attr2 = attrs
    Val.objects.create(product=p1, attr=attr1, label='Toyota')
    Val.objects.create(product=p1, attr=attr2, label='Red')
    Val.objects.create(product=p2, attr=attr1, label='Ford')
    Val.objects.create(product=p2, attr=attr2, label='Blue')

def test1(vals):
    result = Val.objects.pivot()
    assert len(result) == 2

def test2(vals):
    result = Val.objects.pivot()
    assert len(result) == 2
