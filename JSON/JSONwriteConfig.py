import json

'''
docs about python Jason
https://docs.python.org/3/library/json.html#encoders-and-decoders

erforms the following translations in decoding by default:

JSON            Python
object          dict
array           list
string          str
number (int)    int
number (real)   float
true            True
false           False
null            None

print(json.dumps({'name': 'max', 'age': 22}))  #serializing a dict
print(json.dumps(['one', 'two']))  #serializing a list
print(json.dumps(('one', 'two')))  #serializing a tuple
print(json.dumps("Helloworld"))  #serializing a string
print(json.dumps(100))  #serializing an int
print(json.dumps(15.36))  #serializing a float
print(json.dumps(False))  #serializing a bool
print(json.dumps(True))  #serializing a bool
print(json.dumps(None))  #serializing None


a = {
    'name': 'max',
    'age': 22,
    'marks': [90, 50, 80, 40],
    'pass': True,
    'myobject': {
        'color': ('red', 'blue')
    },
    'valid': False
}




with open('demo.json', 'w') as fh:
    fh.write(json.dumps(a, indent=4))

'''


configUART = {
    'Mode': 'Polling',  #may be Interrupt or Polling or DMA_based
    'Baud': 115200,   # may be 2400, 4800, 9600, 14400, 19200, 38400, 57600 or 115200
    'Stopbit': 1,   # may be 1 or 2
    'DataBits': 8,   # may be 5 7 8 or 9
    'Parity': 'odd',  # may be 'even' 'odd' or 'none'
    'Handshake': False,  # using cts rts dtr pins is disabled
    'Buffer': {
        'TxData': "HelloWorld!",
        'RxData': [0]
    },
    'enable': True  # module is active
}




with open('MYuartconfig.json', 'w') as cfg:
    cfg.write(json.dumps(configUART, indent=4))
