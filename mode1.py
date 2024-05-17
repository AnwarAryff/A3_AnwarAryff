from landsites import Land
from algorithms.mergesort import mergesort
from copy import deepcopy

class Mode1Navigator:
    """
    Student-TODO: short paragraph as per
    https://edstem.org/au/courses/14293/lessons/46720/slides/318306
    """

    def __init__(self, sites: list[Land], adventurers: int) -> None:
        """
        Peforms the initialzation of object of Mode 1 class
        Student-TODO: Best/Worst Case
        --> Targeted Worst case: O(N log N) or less
        """
        self.adventurers_count = adventurers
        self.site_nodes = [(site.get_gold()/site.get_guardians(), site) for site in sites]
        self.site_nodes = mergesort(self.site_nodes)

    def select_sites(self) -> list[tuple[Land, int]]:
        """
        Best Case: O(1), Occurs when the first site to enter has the same amount of guar
        target best case: O(log N), target worst case: O(N)
        """
        adventurers_rmg = self.adventurers_count
        selected = []
        i = -1
        while adventurers_rmg > 0 and -i <= len(self.site_nodes):
            most_profit = self.site_nodes[i][1]
            if adventurers_rmg >= most_profit.get_guardians():
                selected.append((most_profit, most_profit.get_guardians()))
                adventurers_rmg -= most_profit.get_guardians()
                i -= 1
            else:
                selected.append((self.site_nodes[i][1], adventurers_rmg))
                break
        return selected
            
    def select_sites_from_adventure_numbers(self, adventure_numbers: list[int]) -> list[float]:
        """
        Student-TODO: Best/Worst Case
        targeted worst case: O(A x N)
        """
        rewards = []
        for adventurers in adventure_numbers:
            i = -1
            trip_reward = 0
            while adventurers > 0 and -i <= len(self.site_nodes):
                most_profit = self.site_nodes[i][1]
                if adventurers >= most_profit.get_guardians():
                    trip_reward += most_profit.get_gold()
                    adventurers -= most_profit.get_guardians()
                    i -= 1
                else:
                    trip_reward += most_profit.get_gold()*(adventurers/most_profit.get_guardians())
                    break
            rewards.append(trip_reward)
        return rewards

    def update_site(self, land: Land, new_reward: float, new_guardians: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        land.set_gold(new_reward)
        land.set_guardians(new_guardians)
