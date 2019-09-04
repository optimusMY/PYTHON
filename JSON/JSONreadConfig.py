import json

with open('MYuartconfig.json', 'r') as cfg:
    cfg_str = cfg.read()
    cfg_values = json.loads(cfg_str)

    print(type(cfg_values))

    # now we can use cfg_values as dict
    print(cfg_values['Baud'])
    print(cfg_values['Mode'])
    print(cfg_values['Parity'])
    print(cfg_values['Handshake'])
    print(cfg_values['Stopbit'])
    print(cfg_values['DataBits'])
    print(cfg_values['enable'])
    print(cfg_values['Buffer'])


