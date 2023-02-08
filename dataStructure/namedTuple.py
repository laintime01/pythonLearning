from typing import NamedTuple

# for functions that maybe changed in the future, use namedtuple as return result
class Address(NamedTuple):
    """Address results"""
    country: str
    province: str
    city: str


def latlon_to_address(lat, lon):
    country = 'China'
    province = 'beijing'
    city = 'beijing'
    return Address(
        country=country,
        province=province,
        city=city,
    )


addr = latlon_to_address(1, 2)

print(addr.country,addr.province,addr.city)
