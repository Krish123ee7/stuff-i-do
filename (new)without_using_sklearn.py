import pandas as pd
import numpy as np
import random as rand
import matplotlib.pyplot as plt

def show_data(X: pd.DataFrame,y:pd.Series|np.ndarray,function = None):
    if list(y.astype(bool).astype("str").unique()) in [["True","False"],["False","True"]]:
        y = y.astype(bool).astype("str")
    print(y)
    no_of_lables = len(X.columns)
    fig, ax = plt.subplots(no_of_lables)
    index = 0
    for col in X.columns:
        ax[index].scatter(y,X[col],alpha=0.3)
        ax[index].set_xlabel("risk")
        ax[index].set_ylabel(col)
        index+=1
    
    plt.show()

def scale_data(data:pd.DataFrame,round_val : int = None,reletive_data:pd.DataFrame = None):
    for col in data.columns:
        try:
            if reletive_data == None:
                max_val = data[col].max()
                min_val = data[col].min()
            else:
                max_val = reletive_data[col].max()
                min_val = reletive_data[col].min()
        except:
            max_val = reletive_data[col].max()
            min_val = reletive_data[col].min()
        
        if round_val == None:
            
            data[col] = (data[col]-min_val)/(max_val-min_val)*100
        else:
            data[col] = (round((data[col]-min_val)/(max_val-min_val)*100,round_val))
    print(min_val,max_val)
    # print(data)
    return pd.DataFrame(data)

def randnum(x):
    try:
        index = rand.randrange(0,x)
    except:
        index = randnum(x)
    return index

def train_test_splitter(X:pd.DataFrame,y,test_ratio = 0.2):
    rows = int(round(len(X)*test_ratio,0))
    X_test = pd.DataFrame(columns=X.columns)
    y_test = []
    X_train = X
    y_train = list(y)
    for i in range(rows):
        try:
            index = randnum(len(X_train))
        except:
            index = 0
        y_test.append(y_train.pop(index))
        values = X_train.values[index]
        X_train.drop(index =index,axis=0,inplace=True)
        X_test.loc[i] = values
        X_train = X_train.reset_index(drop = True)
    
    return X_train,X_test,y_train,y_test

class Node():
    def __init__(self,field,condition,gini,index=None,parent=None):
        self.index = index
        self.parent_node = parent
        self.field = field
        self.condition = condition
        self.gini = gini
        self.is_leaf_node = False
        self.output = None
        self.true_child_node = None
        self.false_child_node = None
        self.sample = 0

class DecisionTreeClassifier():
    def __init__(self):
        self.index = 0
        self.nodes=[]
        self.text = """digraph Tree {
node [shape=box, fontname="helvetica"] ;
edge [fontname="helvetica"] ;"""
    
    def fit(self,X:pd.DataFrame,y:pd.Series,pruning = 0):
        self.X = X
        self.y = y
        self.pruning = pruning
        self.fields = X.columns
        self.fields_dict = {}
        for i in range(len(self.fields)):
            self.fields_dict[self.fields[i]] = i
        self.root = self.next_node(X,y)
        self.root.index = 0
        
        
    
    def next_node(self,X:pd.DataFrame,y:pd.Series,parent:Node = None):
        nodes = []
        for column in X.columns:
            first_turn = True
            previous_value =  None
            count = -1
            for value in X.sort_values(by=column)[column]:
                count+=1
                if first_turn:
                    previous_value = value
                    first_turn = False
                    continue
                if count == self.pruning+1:
                    count = 0
                    nodes.append([column,(value+previous_value)/2])
                    previous_value = value
        for i in nodes:
            true_left = 0
            true_right = 0
            false_left = 0
            false_right = 0
            index =0
            for value in X[i[0]]:
                if list(y)[index] and value <= i[1]:
                    true_left+=1
                elif list(y)[index] and value > i[1]:
                    true_right+=1
                elif not(list(y)[index]) and value <= i[1]:
                    false_left+=1
                elif not(list(y)[index]) and value > i[1]:
                    false_right+=1
                else:
                    print("we fucked up gng")
                    quit()
                index+=1
            
            total_true = true_right+true_left
            total_false = false_right+false_left
            total_right = true_right+false_right
            total_left = true_left+false_left
            total = total_right+total_left

            left_gini = 1 - (true_left/total_left)**2 - (false_left/total_left)**2
            right_gini = 1 - (true_right/total_right)**2 - (false_right/total_right)**2
            total_gini = ((left_gini*total_left/total)+(right_gini*total_right/total))

            i.append(total_gini)
            index+=1
        nodes = pd.DataFrame(nodes,columns=["column","condition","gini"])
        nodes = nodes.sort_values(by="gini")
        
        node = Node(list(nodes["column"])[0],nodes.values[0][1],nodes.values[0][2],self.index,parent)
        node.sample = total
        self.nodes.append(node)
        self.index +=1

        if total*2 <= self.pruning:
            print("leaf")
            node.is_leaf_node =  True
            if total_true <= total_false:
                node.output = False
            else:
                node.output = True
        
        elif not(node.is_leaf_node):

            X_left,y_left,X_right,y_right = self.data_splitter(X,y,node)
            
            try:
                node.true_child_node = self.next_node(X_left,y_left,node)
                node.false_child_node = self.next_node(X_right,y_right,node)
            except:
                node.is_leaf_node = True
                if total_true <= total_false:
                    node.output = False
                else:
                    node.output = True
        return node



    def predict(self,X:pd.DataFrame|pd.Series|list,node:Node = None):
        prediction = []
        if node == None:
            node = self.root
        if type(X) in [pd.Series,list,pd.DataFrame,np.ndarray]:
            if type(X) != pd.DataFrame:
                X = list(X)
                var,X =X,pd.DataFrame(columns=self.fields)
                X.loc[0] = var            
            
            for value in X.values:
                if node.is_leaf_node:
                    
                    prediction.append(node.output)
                else:
                    if value[self.fields_dict[node.field]]<node.condition:
                        prediction.append(self.predict(value,node.true_child_node))
                    else:
                        prediction.append(self.predict(value,node.false_child_node))

            if len(prediction) == 1:
                return bool(prediction[0])
            else:
                return pd.Series(prediction)

        else:
            raise TypeError (f"predict cannot accept {type(X)} object")

    def data_splitter(self,X:pd.DataFrame,y:pd.Series,node):
        X_left = pd.DataFrame(columns=X.columns)
        y_left = []
        X_right = pd.DataFrame(columns=X.columns)
        y_right = []

        index = 0 
        for value in X.values:
            if X[node.field].values[index]<node.condition:
                X_left.loc[index] = value
                y_left.append(list(y)[index])
            elif X[node.field].values[index]>=node.condition:
                X_right.loc[index] = value
                y_right.append(list(y)[index])
            index+=1

        y_left,y_right = pd.Series(y_left),pd.Series(y_right)
        return X_left,y_left,X_right,y_right
    
    def draw_tree(self):
        for node in self.nodes:
            if node.is_leaf_node:
                self.text += f'\n{node.index} [label="{node.output}"];'
            else:
                self.text += f'\n{node.index} [label="{node.field} <= {node.condition} \\n gini = {node.gini} \\n sample = {node.sample}"];'
            if node.index != 0:
                self.text +=f"\n{node.parent_node.index} -> {node.index} ;"
        self.text += "\n}"
        file = open("loan_default_risk_Graph(without_sklearn).dot","w")
        file.write(self.text)
        file.close()
    
def accuracy(prediction,y_test):
    total = len(y_test)
    score = 0
    for i in range(total):
        if list(prediction)[i] == list(y_test)[i]:
            score +=1
    score = score/total
    return float(score)

df = pd.read_csv("file.csv")
df = df.dropna()
X = df.drop("Loan_Default_Risk",axis=1)
y = df["Loan_Default_Risk"]
X = scale_data(X)
X_train,X_test,y_train,y_test = train_test_splitter(X,y)
modle = DecisionTreeClassifier()
modle.fit(X_train,y_train,20)
prediction = modle.predict(X_test)
score = accuracy(prediction,y_test)
print("score =",score)
modle.draw_tree()
