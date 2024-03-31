import requests
from pprint import pprint
from collections import OrderedDict


# class act_field:
#     def __init__(self, name, required=True):
#         self.name = name
#         self.required = required


def main():
    url = 'https://api.sejm.gov.pl/eli/acts/DU/2023/1590'
    response = requests.get(url).json()
    act = OrderedDict()
    # fields = {'ELI': act_field('identyfikator_aktu'),
    #           'pos': act_field('pozycja'),
    #           'year': act_field('rok'),
    #           'publisher': act_field('wydawca'),
    #           'validFrom': act_field('wazne_od', False)
    #           }
    fields = {'ELI': 'identyfikator_aktu',
              'pos': 'pozycja',
              'year': 'rok',
              'publisher': 'wydawca',
              'validFrom': 'wazne_od'
              }
    # for key, field in fields.items():
    #     if field.required:
    #         act.update({f'{field.name}': response[key]})
    #     else:
    #         try:
    #             act.update({f'{field.name}': response[key]})
    #         except:
    #             pass
    for key, field in fields.items():
        try:
            act.update({f'{field}': response[key]})
        except:
            act.update({f'{field}': None})


    pprint(act)


if __name__ == '__main__':
    main()
