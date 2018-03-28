from dao.group_chat_dao import ChatDAO
from dao.user_dao import UserDAO
class ParticipantsDao():
    def __init__(self):
        chatDAO = ChatDAO()
        groups = chatDAO.getGroups()
        self.userDAO = UserDAO()
        users = self.userDAO.getAllUsers()
        self.participants = {} 
        self.participants[groups[1]['id']]={
            users[0][0]: users[0], 
            users[1][0]: users[1],
            users[2][0]: users[2]
        }
        self.participants[groups[2]['id']]={
            users[1][0]: users[1],
            users[3][0]: users[3],
            users[2][0]: users[2]
        }
    def getParticipantsOfGroupById(self, id):
        if id in self.participants:
            return {"Participants": self.participants[id]}
