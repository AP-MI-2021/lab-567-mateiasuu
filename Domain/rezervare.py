def create_rezervare(id , nume , clasa , pret , checkin):
    '''

    :param id: string
    :param nume: string
    :param clasa: string
    :param pret: float
    :param checkin: string
    :return: Dict
    '''
    return {
        "id": id ,
        "nume": nume ,
        "clasa": clasa ,
        "pret" : pret ,
        "checkin": checkin,
    }

def get_id(rezervare):
    '''

    :param rezervare: Dict
    :return: id - string
    '''
    return rezervare['id']
