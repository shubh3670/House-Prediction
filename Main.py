#SGD Will Update the values of beta row by row so new loop have been added
class SGDRegressor():
    def __init__(self,Learning_Rate,epochs):
        self.learning_Rate=Learning_Rate
        self.epochs=epochs
        #self.b=Intercept
        self.b=0
        #self.m=Slopes
        self.m=np.ones(X_train[1].shape)
    def fit(self,xTrain,yTrain):
        B_Slope=0
        M_Slope=0
        for i in range(0,self.epochs):
            for j in range(0,xTrain.shape[0]):
                #edx will randomly select number from 0 to xTrain.shape[0]
                edx=np.random.randint(low=0,high=xTrain.shape[0])
                Y_Pred=np.dot(xTrain[edx],self.m)+self.b
                B_Slope=(-2)*(yTrain[edx]-Y_Pred)
                M_Slope=-2*(np.dot((yTrain[edx]-Y_Pred),xTrain[edx]))
                self.b=self.b-(self.learning_Rate*B_Slope)
                self.m=self.m-(self.learning_Rate*M_Slope)
        print(self.m)
        print(self.b)
    def predict(self,x_Test):
        return np.dot(x_Test,self.m)+self.b
    
