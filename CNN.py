import numpy as np
import matplotlib.pyplot as plt

#--------------------------------------------
# Function to display matrix graphically
#--------------------------------------------

def Marvellous_Display(matrix,title):
    plt.figure(figsize=(4,4))
    plt.imshow(matrix,cmap="gray",interpolation="nearest")
    plt.title(title)
    plt.colorbar()
    
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            plt.text(j,i,f"{matrix[i,j]:.1f}",ha="center",va="center",color="red",fontsize=12)

    plt.show()
    
def Marvellous_line():
    print("\n"+"-"*60)

#----------------------------------------------------
# Function : Convulution with detailed calculations
#----------------------------------------------------
def Marvellous_Convolution(image,kernel):
    
    rows,cols = image.shape
    krows,kcols = kernel.shape
    
    output_rows = rows-krows + 1
    output_cols = cols-kcols + 1

    # output for storing the value after multiplying kernel and region 
    output = np.zeros((output_rows,output_cols))
    
    Marvellous_line()
    print("Step 1 : Convolutional Layer")
    Marvellous_line()
    
    for i in range(output_rows):
        for j in range(output_cols):
            
            region = image[i:i+krows,j:j+kcols] # scan the whole image 
            multiplication = region * kernel
            result = np.sum(multiplication)
            
            output[i][j] = result
            
            print(f"\nRegion position -> Row:{i} Column:{j}")
            print("\nSelected Region : ")
            
            print(region)
            print("\nKernel:")
            print(kernel)
            
            print("\nRegion * Kernal :")
            print("\nSum of all values :",result)
            
    print("\nFinal Convolution Output :")
    print(output)
    
    return output

#-------------------------------------------------------
# ReLU With detailed calculations
#-------------------------------------------------------
def Marvellous_ReLU(data):
    Marvellous_line()
    print("Step 2 : RELU ACTIVATION")
    Marvellous_line()

    output = np.maximum(0,data)
    print("\nInput to ReLU :")
    print(data)
    
    print("\nRule : ReLU(x) = max(0,x)")
    print("\nOutput after ReLU :")
    print(output)
    
    return output

#-----------------------------------------------------
# Function : Max Pooling With Detailed Calculation
#-----------------------------------------------------

def Marvellous_Pooling(data):
    
    rows,cols = data.shape
    
    output_rows = rows // 2
    output_cols = cols // 2
    
    output = np.zeros((output_rows,output_cols))
    
    Marvellous_line()
    print("Step 3 : Max pooling")
    Marvellous_line()
    
    r = 0 
    for i in range(0,rows,2):
        c = 0
        for j in range(0,cols,2):
            block = data[i:i+2,j:j+2]
            
            # Skip incomplete box if any
            if block.shape !=(2,2):
                continue
            max_value = np.max(block)
            output[r][c] = max_value
            
            print(f"\nPooling Block Position -> Row :{r} Column{c}")
            print("\nSelected 2 x 2 Block")
            print(block)
            
            print("\nMaximum value selected = ",max_value)
            
            c = c + 1
        r = r + 1
    print("\nFinal Pooling Output:")
    print(output)
    
    return output


#-----------------------------------------------------
# Function : Flatten with detailed output
#-----------------------------------------------------

def Marvellous_Flatten(data):
    Marvellous_line()
    print("Step 4 : FLATTEN LAYER")
    Marvellous_line()
    
    flat = data.flatten()
    
    print("\nInput to flatten :")
    print(data)
    
    print("\nFlattened Output :")
    print(flat)
    
    return flat
#-------------------------------------------------------------
# Function : Fully Connected Layer with detailed calculations
#-------------------------------------------------------------

def Marvellous_FC(flat_data):
    
    Marvellous_line()
    print("Step 5 : FULLY CONNECTED LAYER")
    Marvellous_line()
    
    # manual weights
    weights = np.array([1,1,1,1],dtype=float)
    bias = 0.0
    
    print("\nFlatten Input :")
    print(flat_data)
    
    print("\nWeights:")
    print(weights)
    
    print("\nBias:")
    print(bias)
    
    multiplication = flat_data * weights
    result = np.sum(multiplication) + bias
    
    print("\nInput * Weights:")
    print(multiplication)
    
    print("\nSum=",np.sum(multiplication))
    print("\nFinal Output After Adding Bias :",result)
    
    return result
    

def Marvellous_CNN():
    print("Choose Input Image")
    print("1 : Vertical Image")
    print("2 : Horizontal Image")
    
    choice = int (input("Enter Your Choice: "))
    
    # Created Vertical Image 
    if choice == 1:
        image = np.array([
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,0,1,0,0]
        ],dtype=float)
        actual = "Vertical Line"
        
    # Created Horizontal image
    else:
        image = np.array([
            [0,0,0,0,0],
            [0,0,0,0,0],
            [1,1,1,1,1],
            [0,0,0,0,0],
            [0,0,0,0,0]
        ],dtype=float)
        actual = "Horizontal Line"
        
    Marvellous_line()
    print("INPUT IMAGE")
    Marvellous_line()
    print("\nActual Input : ",actual)
    print("\nInput Matrix:")
    print(image)
    print("Image Shape : ",image.shape)     
    
    Marvellous_Display(image,"input image")

    #---------------------------------------------
    # Kernal For vertical feature detection
    #---------------------------------------------
    
    kernal = np.array([
        [-1,1,-1],
        [-1,1,-1],
        [-1,1,-1], 
    ],dtype=float)
    
    Marvellous_line()
    print("KERNEL")
    Marvellous_line()
    print("\nKernel Used to detect vertical pattern:")
    print(kernal)
    Marvellous_Display(kernal,"Vertical Detection Kernel")
    
    #---------------------------------------
    # Step 1 : Convolution
    #---------------------------------------
    conv=Marvellous_Convolution(image,kernal)
    
    #---------------------------------------
    # Step 2 : ReLU
    #---------------------------------------
    relu = Marvellous_ReLU(conv)
    Marvellous_Display(relu,"ReLU Output")
    
    #---------------------------------------
    # Step 3 : Pooling
    #---------------------------------------
    pool = Marvellous_Pooling(relu)
    Marvellous_Display(pool,"Pooling Output")
    
    #---------------------------------------
    # Step 4 : Flatten
    #---------------------------------------
    flat = Marvellous_Flatten(pool)
    
    #---------------------------------------
    # Step 5 : Fully Connected Layer
    #---------------------------------------
    score = Marvellous_FC(flat)
    
    #-------------------------------------------
    # Final Prediction Layer
    #-------------------------------------------
    Marvellous_line()
    print("Step 6 : FINAL PREDICTION")
    
    if score > 0 :
        prediction = "Vertical Line"
    else:
        prediction = "Horizontal Line"
    
    print("\nPredicted Output : ",prediction)
    print("Actual Output :",actual)

Marvellous_CNN()