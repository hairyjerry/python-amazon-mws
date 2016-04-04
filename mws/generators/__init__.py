from xml.etree.ElementTree import Element, tostring
from xml.dom import minidom


override = Element('Override')

sku = Element('SKU')
sku.text = 'ayy-lmao-123'
override.append(sku)

shipping_override = Element('ShippingOverride')
override.append(shipping_override)

ship_option = Element('ShipOption')
ship_option.text = 'Std Cont US PO Box'
shipping_override.append(ship_option)


data = minidom.parseString(tostring(override))
print data.toprettyxml()
