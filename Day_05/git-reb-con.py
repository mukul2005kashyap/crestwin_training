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