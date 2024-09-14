import cv2
from skimage.metrics import structural_similarity as ssim
import statistics


def match1(path):
    
    two_dim_image_list=[]
  
    imgg=[]
    for i in range(0, len(path)):
        img=[]
        for j in range(0,len(path[0])):
            # print(str(i)+"  "+str(j))
            # print(path[i][j],end="  ")
            # read the images
            # imgg[i][j] = cv2.imread(path[i][j])
            img.append(cv2.imread(path[i][j]))
        imgg.append(img)
        # img.clear()
        # print("\n"+str(i))
   

    for i in range(0, len(path)):
        for j in range(0,len(path[0])):
            imgg[i][j] = cv2.cvtColor(imgg[i][j], cv2.COLOR_BGR2GRAY)

    for i in range(0, len(path)):
        for j in range(0,len(path[0])):
    # #         # resize images for comparison
            imgg[i][j] = cv2.resize(imgg[i][j], (300, 300))

    two_dim_image_list=imgg
    # for i in range(0, len(path)):
    #     for j in range(0,len(path[0])):
    #         two_dim_image_list[i][j]=img[i][j]
    # #         # display both images
            # cv2.imshow(str(i)+str(j), imgg[i][j])
           
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
           

    print(two_dim_image_list)
    
    # similarity_avg_value = average_ssim(image_list)
    similarity_value_list = average_ssim(two_dim_image_list)
    

    return similarity_value_list



def average_ssim(two_dim_image_list):
    total_ssim = 0
    pairs_count = 0
   
    two_dim_percent_list=[]
    
    # Compute SSIM for all pairwise combinations
    for i in range(0,len(two_dim_image_list)):  #responsibility to take over to next list inside 2d list
        percent_list=[]
        for j in range(0, len(two_dim_image_list[0])):
            for k in range(j+1, len(two_dim_image_list[0])):
                ssim_score = ssim(two_dim_image_list[i][j], two_dim_image_list[i][k])*100 +5

                #peeking indivisual match percentages inside the percent list
                if(j==0):
                    percent_list.append(round(ssim_score, 2))
                    # two_dim_percent_list.append(percent_list)
                total_ssim += ssim_score
                pairs_count += 1

        two_dim_percent_list.append(percent_list)
    # avg_ssim=statistics.mean(percent_list)
    print(two_dim_percent_list)
    print(len(two_dim_percent_list))

    return two_dim_percent_list




# def compute_ssim(img1, img2):
#     ssim = cv2.SSIM(img1, img2)
#     return ssim