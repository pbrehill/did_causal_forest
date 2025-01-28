from cart import CART

class Ctree(CART):
    def emse_gain(Y, W, split, tr_est_ratio):
        Nl = len(Y)
        
    def _leaf_gain(Y, W, Nl, )


class CtreeSplitter():
    def __init__(Y, W, split, tr_est_ratio, sample_nums):
        self.Y = Y,
        self.W = W, 
        self.split = split,
        self.tr_est_ratio = tr_est_ratio
        self.Nl = len(Y)
        self.sample_nums = sample_nums 

    def emse_gain():
        return (np.mean(split == 1) * self._leaf_gain(1)) + (np.mean(split == 0) * self._leaf_gain(0))

    def _leaf_gain(side):
        if side != 0 or side != 1:
            raise ValueError
        
        leaf_size = self.Nl * np.mean(split == side)
        mu1 = np.mean(Y[split == side and W == 1])
        mu0 = np.mean(Y[split == side and W == 0])
        tau2 = (mu1 - mu0)^2
        return tau2 - self.sample_nums * (
                (np.var(Y[split == side and W == 1])/tr_est_ratio) + 
                (np.var(Y[split == side and W == 0])/(1 - tr_est_ratio))  
        )
            
