#Docker  
"""
docker is a tool that provide you a simplified process to how to develop adnd packaacgge and deploy you app inside the container

conatiner is the lightweight peice of s/w tthat contain the code muktiple dependencies and libraiies that would be needed to run 
that appliction 


? why we need docker :

    so basically that encapasulate all the things that required to run thaat appliacations 

    so in docker  can deploy your website on multiple machines.. 


? Docker demain :
        docler demain is the backgourand service that runs on the host macnhine , it manages the docker objects ,images , container , vovlume etc...


? Docker Images :
        Docker iamges are the stand alone , lightweight executable software package that include everything that are nedded to run the
        the peice of software , like ecvironment variables dependencies ,runtime libraries configurations etc .. 
            that images are used to crate the docker container that are instaced of this images ...
                Image component :
                    base image 
                    application code 
                    dependencies 
                    metadata

? life cycle of the docker image :
    createation 
    storage 
    distribution 
    executions

? Docker file :
     docker file contain the series of instruction that are used to build the docker images , and each instruction in docker file create the layer of image 
     you can say that the docker file are used to automate the image creations process

? docker registery 

        docker registery are the the service that stores and distribute the docker images . it act as the repo where the user can push pull and manage the docker 
        images 


? creating a docker images
    
    docker commands ::
            docker pull IMAGE_NAME

            docker images

            docker run IMAGE NAME                  ---we can create the multiple contanier form our docker images, contianer and images are like the objects and class

            docker run -it IMAGE NAME    -- it is used to start the container in the interactive mode -i keeps the stdin opne sp we can give the input and -t keeps the 
                                            allocate the terminal that provide the proper shell environment inside the terminal ...
                                                    it is basically used for the debugging , manual testing , and when we want to use the command intternally inside the 
                                                    containetr 
            
            docker ps -a             

            docker start IMAGE_NAME / ID            it will start the existing container via container name or their id 

            docker stop IMAGE NAME / ID             it will stop the running continer via container name or  id 

            docker rmi IMAGE NAME /ID               IT will remove or destroy the image 

            docler rm CONTAINER NAME /ID            it will remove or destory the container 

!        :: before revomeing or destorying the image you are needed to remove the existing container of that image ::

            docker pull IMAGE NAME:VERSION          THROUGH this you can create same image for another version 

?       port Binding ::- PORT bindidng means mapping the containers internal port to the host machines port so the external traffic can also access the 
?                        application running inside the container .
            
            docker run -p8080:3306 IMAME   AGE N    by this cmd you can bind your container to the host port .

            docker logs CONT.ID                     if you encounter to the error then through this command you will see all the logs 
            

"""
# docker desktop

"""
docker desktop contain the small linux based virtual machine that help us to run our container 
"""





# RBAC :: Role based access control 
"""
rbac is an authentication machanism where permissions ae asign to the roles ineasted of asign them to the 
users Users inherit permissions based on the roles they are assigned. It simplifies access management, 
improves security, and scales well in enterprise systems.

    “In large systems, managing permissions individually for every user becomes complex and error-prone.
     To solve this, we use Role-Based Access Control.”

    “RBAC mainly has three components: User, Role, and Permission.”

            User – Person using the system

            Role – Job function (Admin, Analyst, ML Engineer)

            Permission – Allowed actions (Read, Write, Delete, Deploy)

?       for example 

            Admin can manage users and models

            ML Engineer can deploy models

            Analyst has read-only dashboard access
            If a new ML engineer joins, we simply assign the ML Engineer role, and required permissions are automatically inherited



"""

# middleware

"""
Middleware 
    middleware is a software layer that works between the two applicatons or websites and also process and manage and transform 
    the between that websites 
    
    so in simpele words we can say that the middlewate is intermediarya that works between the request and reponse
    so you can say that the middleware is performs the tsk like logging authentication and also the data trasformation 

Key Functions of Middleware

Authentication & Authorization
    Verify users and control access to resources.

Logging & Monitoring
    Track incoming requests, responses, and errors for analytics.

Error Handling
    Catch exceptions and send consistent error messages.

Data Transformation
    Modify requests or responses (e.g., JSON formatting, header changes).

Caching
    Store frequently accessed data to improve performance.
"""
