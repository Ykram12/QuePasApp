# QuePasApp
Social network application

With this application users will be able to chat with each other through message posts in group chats. Also, users will be able to add other users to their contact lists for future reference when creating a group chat. Reactions for chat messages are possible (like and dislike) and possibly the user could post a message with an image or video. 

## ER Diagram

Our ER Diagram consists of 3 Main Entitities: Users, Groups and Messages. Related to these you also have the Reactions entity and various other relations between the entities such as: Participant, Creates, Posts, Read by, Makes, Contains, Has, Reply.

![alt text](https://i.imgur.com/I9aHxxQ.jpg "QuePasApp - ER Diagram")

### Users **Participant** Groups
This entity will have a participant table because many users can belong to many groups. The participant relationship will be mapped using the User's id and the Group's ids to create the table's primary key. 

### Users **Creates** Groups
A creates relationship with Groups is defined because one user will be able to create many groups. The creates relationship will not be mapped because it is a one to many relationship with total participation. The Groups entity will contain an attribute that will be a foreign key of the chat creator's id (owner).

### Users **Posts** Messages
A posts relationship will be held with the Messages entity to be able to keep track of who has posted what message. Mapping Posts is not necessary due to it being a one to many relationship with total participation. Messages will contain an attribute that will be a foreign key of the message writers id.

### Users **Read by** Messages
A read by relationship will be held with the Messages entity to be able to keep track of who has read what message and when. In the case of the Read By relationship we need to map it and we utilize the readers id, the messages id, and the time and date it was read. Using the readers id and the messages id we create a primary key for this relation.

### Users **Makes** Reactions
A makes relationship will be held between Users and Reactions to be able to keep track of what reaction  was done by which user to what meessage. This table will contain a serial primary key and references to the writers id and to the messages id.

### Groups **Contains** Messages
A contains relationship was defined between Groups and Messages because every group will contain a list of messages. This relationship will not be mapped because of it being a one to many relationship with total participation. Messages will contain a foreign key that will reference the group where the message is contained.

### Messages **Has** Reaction
Knowing that messages will have reactions we defined a relationship between these. As previosly mentioned in other relationship, this one will not be mapped either because of it being a one to many relationship with total participation. Reaction will contain the message id of the message it belongs to.

## API Routing

Designing a mockup of what the API implementation could be was important for the development of the backend. Using swaggerhub we were able to prepare the design of the API. [View in this link](https://app.swaggerhub.com/apis/Ykram12/QuePasApp/1.0.0#/)

## Story Map

A projection of the web-applications development was done. Although due to the way phases are delivered we may not follow this story map strictly. 

![alt text](https://i.imgur.com/TpUXHln.jpg "QuePasApp - Story Map")

