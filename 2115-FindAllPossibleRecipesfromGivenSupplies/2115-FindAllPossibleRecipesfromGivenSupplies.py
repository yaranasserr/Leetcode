class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # adj = {r: [ing] for r, ing in zip(recipes, ingredients)}
        recipe_index = {r : i for i,r in enumerate(recipes)}
        can_cook = {s:True for s in supplies} # r -> T/F 
        # check if i can cook r with the supplies i have 

        def dfs(r):
            if r in can_cook :
                return can_cook[r]
            can_cook[r] = False # circular 

            if r not in recipe_index:
                return False 

            for nei in ingredients[recipe_index[r]]:

                if not dfs(nei):
                    return False

            can_cook[r] = True 

            return can_cook[r]




        # for r in recipes:
        #     if dfs(r):
        #         res.append(r)

        # return res 

        return [ r for r in recipes if dfs(r)]




        # # adj list : key[recipe] , values :ingredients
        # adj = {r:[] for r in range(len(recipes))}
        
        # for i in range(len(ingredients)):
        #     adj[i].append(ingredients[i])

        # adj = dict(zip(recipes, adj.values()))
        # adj = {r: [ing] for r, ing in zip(recipes, ingredients)}





        