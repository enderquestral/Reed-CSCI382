G1 = [A,D,G,J]
G2 = [B,E,H,K]
G3 = [C,F,I,L]

WEIGH G1 vs G2:
    if Balance, then counterfeit is in G3:
        WEIGH C,F,I against A,D,J
        if Balanced:
            Coin L is counterfeit
        else:
            if C,F,I is heavy:
                WEIGH C vs F.
                if Balanced:
                    Coin I is counterfeit
                else:
                    heavier coin is counterfeit
            if C,F,I is light:
                WEIGH C vs F.
                if Balanced:
                    Coin I is counterfeit
                else:
                    lighter coin is counterfeit
    
                                
    else:
        if G2 is heavy:
            WEIGH A,B,E against D,K,H.
            if Balanced: #G or J is fake
                WEIGH J vs C.
                if Balanced:
                    Coin G is counterfeit
                else:
                    Coin J is counterfeit
            else:
                if D,K,H is heavy: #Different coin is K,H,A
                    WEIGH K vs H
                    if Balanced:
                        Coin A is counterfeit
                    else:
                        heavier count is counterfeit

                if D,G,H is lighter: #Different coun is B,E,D
                    WEIGH B vs E
                    if Balanced:
                        Coin D is counterfeit
                    else:
                        lighter count is counterfeit


        else if G1 is heavy:
            WEIGH B,A,D against E,J,K.
            if Balanced: #H or K is fake
                WEIGH H vs C.
                if Balanced:
                    Coin K is counterfeit
                else:
                    Coin H is counterfeit
            else:
                if E,J,K D,K,H is heavy: #Different coin is J,K,B
                    WEIGH J vs K
                    if Balanced:
                        Coin B is counterfeit
                    else:
                        heavier count is counterfeit

                if E,J,K is lighter: #Different coin is A,D,E
                    WEIGH A vs D
                    if Balanced:
                        Coin E is counterfeit
                    else:
                        lighter count is counterfeit
            

