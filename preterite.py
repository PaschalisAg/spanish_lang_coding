import time

# el pretérito o el pretérito perfecto simple


def preterito():
    """
    El pretérito o el pretérito perfecto simple:
    - The pretérito is NOT used when we want to talk about
    continuous or habitual actions in the past with no specific
    beggining or end. In this case the pretérito imperfecto is used.

    - completed events
    - beginnings and ends
    - specific times and dates
    - events in sequence

    The regular conjugation of the 'pretérito' follows these rules:
        - remove the infinitive ending (i.e., -ar, -er, -ir)
        - if -ar verb:
            >  verb + ['é', 'aste', 'ó', 'amos', 'asteis', 'aron']
        - if -er/-ir verb:
            >  verb + ['í', 'iste', 'ió', 'imos', 'isteis', 'ieron']

    There are 4 irregular verbs in 'pretérito': ser, ir, dar, ver
    ser: fui, fuiste, fue, fuimos, fuisteis, fueron
    ir: fui, fuiste, fue, fuimos, fuisteis, fueron
    dar: di, diste, dio, dimos, disteis, dieron
    ver: vi, viste, vio, vimos, visteis, vieron
    """
    verb = str(input("Darme un infinitivo en Castellano:")).strip().lower()
    ser_ir_preterito = ["fui", "fuiste", "fue", "fuimos", "fuisteis", "fueron"]
    dar_preterito = ["di", "diste", "dio", "dimos", "disteis", "dieron"]
    ver_preterito = ["vi", "viste", "vio", "vimos", "visteis", "vieron"]
    ar_suffixes = ["é", "aste", "ó", "amos", "asteis", "aron"]
    er_ir_suffixes = ["í", "iste", "ió", "imos", "isteis", "ieron"]
    # IRREGULAR VERBS
    # ser and ir
    if verb == "ser" or verb == "ir":
        for case in ser_ir_preterito:
            print(case)
            time.sleep(1)
    elif verb == "dar":
        for case in dar_preterito:
            print(case)
            time.sleep(1)
    elif verb == "ver":
        for case in ver_preterito:
            print(case)
    # REGULAR VERBS
    # verbs that end with -ar
    elif verb.endswith("ar"):
        for suffix in ar_suffixes:
            print(verb[:-2] + suffix)
            time.sleep(1)
    elif verb.endswith(("er", "ir")):
        if verb
        for suffix in er_ir_suffixes:
            print(verb[:-2] + suffix)
            time.sleep(1)
    else:
        raise ValueError(
            'Verb is not in infinitive form. Remember that verbs in Spanish can end in -ar, -er, -ir')


preterito()
