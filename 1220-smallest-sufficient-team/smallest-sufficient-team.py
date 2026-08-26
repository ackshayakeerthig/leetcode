class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        m=len(req_skills)
        skill_id={skill : i for i,skill in enumerate(req_skills)}

        people_mask=[]
        for person in people:
            mask=0
            for skill in person:
                mask|=(1<<skill_id[skill])
            people_mask.append(mask)
        full_mask=(1<<m)-1

        #dp[mask]= list of people forming the skill set chosen in mask
        dp=[None]*(1<<m)
        dp[0]=[]
        for i in range(len(people)):
            person_mask=people_mask[i]
            for mask in range(full_mask,-1,-1):
                if dp[mask]==None:
                    continue
                new_mask=mask|person_mask
                if dp[new_mask]==None or len(dp[new_mask])>len(dp[mask])+1:
                    dp[new_mask]=dp[mask]+[i]
        return dp[full_mask]