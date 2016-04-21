dataDictionary = {
  'SMOKE100': {
    '': 'missing',
    '1': 'smoker',
    '2': 'never smoked',
    '7': "don't know",
    '9': 'refused'
  },
  'GENHLTH' : {
    '': 'missing',
    '1': 'excellent',
    '2': 'very good',
    '3': 'good',
    '4': 'fair',
    '5': 'poor',
    '7': "don't know",
    '9': 'refused'
    },
  'POORHLTH' : {
    '': 'missing',
    '88': 'none',
    '77': "don't know",
    '99': 'refused'
    },
  'EXERANY2' : {
    '' : 'missing',
    '1': 'yes',
    '2': 'no',
    '7': "don't know",
    '9': 'refused'
    },
  'SLEPTIM1' : {
    '': 'missing',
    '77': "don't know",
    '99': 'refused'
  },
  'SEX' : {
    '1': 'male',
    '2': 'female',
  },
  'SMOKEDAY2' : {
    '': 'missing',
    '1': 'every day',
    '2': 'some days',
    '3': 'not at all',
    '7': "don't know",
    '9': 'refused'
  },
  'AVERDRNK2' : {
     '': 'missing',
    '77': "don't know",
    '99': 'refused'
  },
  'MAXDRNKS'  : {
     '': 'missing',
    '77': "don't know",
    '99': 'refused'
  },
  "_STATE" : {
    '9': 'CT',
    '37': 'NC'
  }
}

def mapResponse (var, value):
  ''' function to assign response value mappings from dataDictionary to data'''
  newlabel=value
  if var in dataDictionary:
    if value in dataDictionary[var]:
      newlabel = dataDictionary[var][value] # remaps values from raw number to label, if number not mapped, actual value remains - because newlabel is set to value above
  return newlabel