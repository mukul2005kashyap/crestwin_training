# REBASE
"""
git rebase is cmnd that moves or replay your branch commit on the top of the latest branch commit
 like main branch or another else 

        for example you have a main branch and you create another feature branch then there is something commits are
          made in the main branch then you want to get all the commits to add in your feature branch then you just 

?                        checkout the feature branch
                            git rebase <main>

this command add like merge the main branch commit in your feature branch without adding the new commit in your main branch  
        
 """
 

# FAST FORWARD MERGE

"""
as if you rebase the feature branch into the main branch then it create problem like it rewrite the commits into the main and delete the 
previous commmits 

        best practice in that case you just do merge 
        or you can do the fast forward mergre

?                                    checkout the main branch and 
?                                    git merge-ff-only <feature -branch>

"""

# shell automation

"""
shell automation is the process of      using the shell script or a bash script to automate the repetative task likke
                process management 
                deployement 
                regulary backup check 
                monitoring 
                log file cleaning 
                server restart and server check 

                
                """

# shell automation in linux primarly uses the shell scripting which involves writting the series of command in text file
# for shell to perform automattically

# ?  Benifits of automation
#               it increases the effeciancy and improved conscitency by reduciung human error and scalability , enhanced 
#               relabilitty of task like system monitoring and backup etc.....


"""
for example :
        sudo apt update -y              --this file download the laatest packages from the current repo

        sudo apt upgrade -y             -- this installs the available updates for already installed packages

        sudo apt autoremove -y          --This removes unnecessary packages that were installed as dependencies

        echo "System update completed."
 

        """

