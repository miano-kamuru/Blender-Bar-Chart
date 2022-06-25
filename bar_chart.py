#author:miano kamuru
import bpy
from math import radians

bucket=[ #-------------------data to read
{'Country': 'Angola', 'CPI': [27, 26, 19, 19, 18.0, 15.0, 19.0, 23.0, 22.0]},
{'Country': 'Botswana', 'CPI': [60, 61, 61, 61, 60.0, 63.0, 63.0, 64.0, 65.0]},
{'Country': 'Lesotho', 'CPI': [41, 40, 41, 42, 39.0, 44.0, 49.0, 49.0, 45.0]},
{'Country': 'Madagascar', 'CPI': [25, 24, 25, 24, 26.0, 28.0, 28.0, 28.0, 32.0]},
{'Country': 'Malawi', 'CPI': [30, 31, 32, 31, 31.0, 31.0, 33.0, 37.0, 37.0]},
{'Country': 'Mauritius', 'CPI': [53, 52, 51, 50, 54.0, 53.0, 54.0, 52.0, 57.0]},
{'Country': 'Mozambique', 'CPI': [25, 26, 23, 25, 27.0, 31.0, 31.0, 30.0, 31.0]},
{'Country': 'Namibia', 'CPI': [51, 52, 53, 51, 52.0, 53.0, 49.0, 48.0, 48.0]},
{'Country': 'Seychelles', 'CPI': [66, 66, 66, 60, 0, 55.0, 55.0, 54.0, 52.0]},
{'Country': 'South Africa', 'CPI': [44, 44, 43, 43, 45.0, 44.0, 44.0, 42.0, 43.0]}
]
read={"label_xAxis":"Country", #how to read the data 
      "Values":"CPI",
      "label_yAxis":'Ýears',
      "data_yAxis":['2012','2013','2014','2015','2016','2017','2018','2019','2020']
    }

        
def makeBars(row,y,heightScale,spacing=1,label_thickness=0): #make bars
  bar_size=1
  count=0
  for bar in bucket:
    bpy.ops.mesh.primitive_cube_add(location=((spacing)*(count*(bar_size*2)),y*spacing,0),
    scale=(bar_size,
           bar_size,
           bar[read['Values']][row]/heightScale)) #create_bars 
           
    #change the origin
    bpy.ops.object.editmode_toggle()
    bpy.ops.transform.translate(value=(0, 0, bar[read['Values']][row]/heightScale), orient_axis_ortho='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
    bpy.ops.object.editmode_toggle()
    #---------------------------------#
    #make label in the x axis
    bpy.ops.object.text_add()
    label=bpy.context.object
    label.data.body = bucket[count][read["label_xAxis"]]
    label.location[0]=(spacing)*(count*(bar_size*2))
    label.location[1]=-1
    label.location[2]=0
    label.rotation_euler[2]+=radians(-90)
    if(label_thickness!=0 and label_thickness>0):
     #add the solidify modifier
     bpy.ops.object.modifier_add(type='SOLIDIFY')
     label.modifiers["Solidify"].thickness = label_thickness
    


    #-------------------------------------#
    count+=1
  #make labels in the y axis 
  count=0
  while(count<len(read['data_yAxis'])):
      bpy.ops.object.text_add()
      labelY=bpy.context.object
      labelY.data.body = read['data_yAxis'][count]
      labelY.location[0]=(((-bar_size))*1.05)
      labelY.location[1]=(spacing)*(count*(bar_size*2))
      labelY.location[2]=0
      labelY.rotation_euler[2]+=radians(180)
      if(label_thickness!=0 and label_thickness>0):
         bpy.ops.object.modifier_add(type='SOLIDIFY')
         labelY.modifiers["Solidify"].thickness = label_thickness
      count+=1

    
    

def create(spacing,heightScale=1): #create bar chart
  bar_size=1
  count=0 
  if len(read['data_yAxis'])==0:  
     makeBars(count,count*2,heightScale=heightScale,spacing=spacing)
  else:
      while(count<len(read['data_yAxis'])):
        makeBars(count,count*2,heightScale=heightScale,spacing=spacing,label_thickness=0)
        count+=1

  
create(heightScale=10,spacing=1.25)


   
        





  