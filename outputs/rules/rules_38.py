def findDecision(obj): #obj[0]: Age, obj[1]: Total_Bilirubin, obj[2]: Direct_Bilirubin, obj[3]: Alkaline_Phosphotase, obj[4]: Alamine_Aminotransferase, obj[5]: Aspartate_Aminotransferase, obj[6]: Total_Protiens, obj[7]: Albumin, obj[8]: Albumin_and_Globulin_Ratio
   # {"feature": "Age", "instances": 519, "metric_value": 0.0, "depth": 1}
   if obj[0]>44.323699421965316:
      # {"feature": "Albumin", "instances": 270, "metric_value": 0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Alkaline_Phosphotase", "instances": 152, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Aspartate_Aminotransferase", "instances": 117, "metric_value": 0.0, "depth": 4}
            if obj[5]<=54.30769230769231:
               # {"feature": "Total_Protiens", "instances": 86, "metric_value": 0.0, "depth": 5}
               if obj[6]>60.08139534883721:
                  # {"feature": "Total_Bilirubin", "instances": 64, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=8:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 43, "metric_value": -0.0, "depth": 7}
                     if obj[8]>7:
                        # {"feature": "Alamine_Aminotransferase", "instances": 29, "metric_value": -0.0, "depth": 8}
                        if obj[4]>10:
                           return 'liver'
                        elif obj[4]<=10:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[8]<=7:
                        # {"feature": "Alamine_Aminotransferase", "instances": 14, "metric_value": -0.0, "depth": 8}
                        if obj[4]>18:
                           return 'liver'
                        elif obj[4]<=18:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[1]>8:
                     # {"feature": "Direct_Bilirubin", "instances": 21, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=7:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 20, "metric_value": -0.0, "depth": 8}
                        if obj[8]>9:
                           return 'liver'
                        elif obj[8]<=9:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>7:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[6]<=60.08139534883721:
                  # {"feature": "Alamine_Aminotransferase", "instances": 22, "metric_value": 0.0, "depth": 6}
                  if obj[4]>17:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 18, "metric_value": 0.0, "depth": 7}
                     if obj[8]>9:
                        # {"feature": "Total_Bilirubin", "instances": 12, "metric_value": -0.0, "depth": 8}
                        if obj[1]>8:
                           return 'normal'
                        elif obj[1]<=8:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]<=9:
                        # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[1]>6:
                           return 'liver'
                        elif obj[1]<=6:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=17:
                     # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=1:
                        return 'normal'
                     elif obj[2]>1:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=7:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'normal'
            elif obj[5]>54.30769230769231:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 31, "metric_value": -0.0, "depth": 5}
               if obj[8]>7:
                  # {"feature": "Total_Protiens", "instances": 18, "metric_value": -0.0, "depth": 6}
                  if obj[6]<=71:
                     # {"feature": "Alamine_Aminotransferase", "instances": 15, "metric_value": -0.0, "depth": 7}
                     if obj[4]>28:
                        # {"feature": "Total_Bilirubin", "instances": 10, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=16:
                           return 'liver'
                        elif obj[1]>16:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=28:
                        # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": -0.0, "depth": 8}
                        if obj[2]>2:
                           return 'liver'
                        elif obj[2]<=2:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[6]>71:
                     # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[1]>8:
                        return 'liver'
                     elif obj[1]<=8:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[8]<=7:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 35, "metric_value": 0.0, "depth": 4}
            if obj[8]>8:
               # {"feature": "Total_Bilirubin", "instances": 19, "metric_value": -0.0, "depth": 5}
               if obj[1]<=24:
                  # {"feature": "Alamine_Aminotransferase", "instances": 13, "metric_value": -0.0, "depth": 6}
                  if obj[4]>36:
                     return 'liver'
                  elif obj[4]<=36:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[5]>17:
                        # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=17:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[1]>24:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[8]<=8:
               return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      elif obj[7]<=26.393063583815028:
         # {"feature": "Direct_Bilirubin", "instances": 118, "metric_value": 0.0, "depth": 3}
         if obj[2]>1:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 102, "metric_value": -0.0, "depth": 4}
            if obj[8]<=14.049019607843137:
               # {"feature": "Alkaline_Phosphotase", "instances": 87, "metric_value": -0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Alamine_Aminotransferase", "instances": 60, "metric_value": 0.0, "depth": 6}
                  if obj[4]<=45.266666666666666:
                     # {"feature": "Total_Bilirubin", "instances": 45, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=22.755555555555556:
                        # {"feature": "Total_Protiens", "instances": 31, "metric_value": -0.0, "depth": 8}
                        if obj[6]>10.481176377641233:
                           return 'liver'
                        elif obj[6]<=10.481176377641233:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>22.755555555555556:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]>45.266666666666666:
                     # {"feature": "Total_Protiens", "instances": 15, "metric_value": -0.0, "depth": 7}
                     if obj[6]<=56:
                        # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": -0.0, "depth": 8}
                        if obj[1]>13:
                           return 'liver'
                        elif obj[1]<=13:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[6]>56:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[5]>32:
                           return 'liver'
                        elif obj[5]<=32:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[3]>291.0539499036609:
                  # {"feature": "Total_Protiens", "instances": 27, "metric_value": 0.0, "depth": 6}
                  if obj[6]>26.5270765613015:
                     # {"feature": "Alamine_Aminotransferase", "instances": 22, "metric_value": -0.0, "depth": 7}
                     if obj[4]>12:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 21, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=258.7142857142857:
                           return 'liver'
                        elif obj[5]>258.7142857142857:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=12:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[6]<=26.5270765613015:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[8]>14.049019607843137:
               # {"feature": "Alkaline_Phosphotase", "instances": 15, "metric_value": 0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Total_Bilirubin", "instances": 9, "metric_value": 0.0, "depth": 6}
                  if obj[1]>5:
                     # {"feature": "Alamine_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=30:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=32:
                           return 'liver'
                        elif obj[5]>32:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>30:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=5:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[3]>291.0539499036609:
                  # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 6}
                  if obj[4]>16:
                     # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=8:
                        return 'liver'
                     elif obj[1]>8:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=63:
                           return 'liver'
                        elif obj[5]>63:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[4]<=16:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[2]<=1:
            # {"feature": "Alamine_Aminotransferase", "instances": 16, "metric_value": -0.0, "depth": 4}
            if obj[4]>24:
               # {"feature": "Aspartate_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 5}
               if obj[5]>23:
                  # {"feature": "Alkaline_Phosphotase", "instances": 7, "metric_value": 0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[1]>4:
                        # {"feature": "Total_Protiens", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[6]>4:
                           return 'liver'
                        elif obj[6]<=4:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=4:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[3]>291.0539499036609:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[5]<=23:
                  return 'normal'
               else:
                  return 'normal'
            elif obj[4]<=24:
               # {"feature": "Aspartate_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 5}
               if obj[5]<=34:
                  # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": -0.0, "depth": 6}
                  if obj[1]>5:
                     return 'liver'
                  elif obj[1]<=5:
                     # {"feature": "Alkaline_Phosphotase", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[3]>291.0539499036609:
                        return 'normal'
                     elif obj[3]<=291.0539499036609:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               elif obj[5]>34:
                  # {"feature": "Alkaline_Phosphotase", "instances": 4, "metric_value": 0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[1]>6:
                        return 'liver'
                     elif obj[1]<=6:
                        # {"feature": "Total_Protiens", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[6]>5:
                           return 'normal'
                        elif obj[6]<=5:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      else:
         return 'liver'
   elif obj[0]<=44.323699421965316:
      # {"feature": "Albumin", "instances": 249, "metric_value": 0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Alkaline_Phosphotase", "instances": 154, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Total_Protiens", "instances": 116, "metric_value": 0.0, "depth": 4}
            if obj[6]<=84.16676164311447:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 109, "metric_value": -0.0, "depth": 5}
               if obj[8]>1:
                  # {"feature": "Direct_Bilirubin", "instances": 90, "metric_value": 0.0, "depth": 6}
                  if obj[2]>1:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 78, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=152.2051282051282:
                        # {"feature": "Alamine_Aminotransferase", "instances": 63, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=40.98412698412698:
                           return 'normal'
                        elif obj[4]>40.98412698412698:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>152.2051282051282:
                        # {"feature": "Alamine_Aminotransferase", "instances": 15, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=179:
                           return 'liver'
                        elif obj[4]>179:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]<=1:
                     # {"feature": "Alamine_Aminotransferase", "instances": 12, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=82:
                        # {"feature": "Total_Bilirubin", "instances": 10, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=6:
                           return 'liver'
                        elif obj[1]>6:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]>82:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]>6:
                           return 'normal'
                        elif obj[1]<=6:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[8]<=1:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 19, "metric_value": 0.0, "depth": 6}
                  if obj[5]>19:
                     # {"feature": "Alamine_Aminotransferase", "instances": 15, "metric_value": -0.0, "depth": 7}
                     if obj[4]>27:
                        # {"feature": "Total_Bilirubin", "instances": 10, "metric_value": -0.0, "depth": 8}
                        if obj[1]>7:
                           return 'liver'
                        elif obj[1]<=7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=27:
                        # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=17:
                           return 'liver'
                        elif obj[1]>17:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[5]<=19:
                     # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=8:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>8:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]>2:
                           return 'normal'
                        elif obj[2]<=2:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[6]>84.16676164311447:
               # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 5}
               if obj[1]<=7:
                  return 'liver'
               elif obj[1]>7:
                  # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=2:
                     # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[4]>15:
                        return 'normal'
                     elif obj[4]<=15:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               else:
                  return 'normal'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Total_Bilirubin", "instances": 38, "metric_value": 0.0, "depth": 4}
            if obj[1]<=24:
               # {"feature": "Alamine_Aminotransferase", "instances": 33, "metric_value": -0.0, "depth": 5}
               if obj[4]<=101.3030303030303:
                  # {"feature": "Direct_Bilirubin", "instances": 22, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=3:
                     # {"feature": "Total_Protiens", "instances": 19, "metric_value": -0.0, "depth": 7}
                     if obj[6]<=72:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 10, "metric_value": 0.0, "depth": 8}
                        if obj[8]<=9:
                           return 'liver'
                        elif obj[8]>9:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[6]>72:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 9, "metric_value": 0.0, "depth": 8}
                        if obj[5]>16:
                           return 'liver'
                        elif obj[5]<=16:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[2]>3:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[8]>7:
                        return 'liver'
                     elif obj[8]<=7:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[4]>101.3030303030303:
                  # {"feature": "Total_Protiens", "instances": 11, "metric_value": 0.0, "depth": 6}
                  if obj[6]<=72:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[5]>231:
                        return 'liver'
                     elif obj[5]<=231:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[8]>1:
                           return 'normal'
                        elif obj[8]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[6]>72:
                     # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": -0.0, "depth": 7}
                     if obj[2]>1:
                        return 'liver'
                     elif obj[2]<=1:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[1]>24:
               return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      elif obj[7]<=26.393063583815028:
         # {"feature": "Alkaline_Phosphotase", "instances": 95, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 70, "metric_value": 0.0, "depth": 4}
            if obj[8]<=9:
               # {"feature": "Direct_Bilirubin", "instances": 53, "metric_value": -0.0, "depth": 5}
               if obj[2]<=2:
                  # {"feature": "Total_Protiens", "instances": 31, "metric_value": -0.0, "depth": 6}
                  if obj[6]>43:
                     # {"feature": "Total_Bilirubin", "instances": 19, "metric_value": -0.0, "depth": 7}
                     if obj[1]>6:
                        # {"feature": "Alamine_Aminotransferase", "instances": 12, "metric_value": 0.0, "depth": 8}
                        if obj[4]>18:
                           return 'normal'
                        elif obj[4]<=18:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=6:
                        # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[4]>12:
                           return 'normal'
                        elif obj[4]<=12:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[6]<=43:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 12, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=28:
                        # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": -0.0, "depth": 8}
                        if obj[4]>21:
                           return 'liver'
                        elif obj[4]<=21:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>28:
                        # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[4]>16:
                           return 'liver'
                        elif obj[4]<=16:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[2]>2:
                  # {"feature": "Total_Protiens", "instances": 22, "metric_value": -0.0, "depth": 6}
                  if obj[6]<=54:
                     # {"feature": "Alamine_Aminotransferase", "instances": 18, "metric_value": -0.0, "depth": 7}
                     if obj[4]>38:
                        # {"feature": "Total_Bilirubin", "instances": 9, "metric_value": 0.0, "depth": 8}
                        if obj[1]>16:
                           return 'liver'
                        elif obj[1]<=16:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=38:
                        # {"feature": "Total_Bilirubin", "instances": 9, "metric_value": 0.0, "depth": 8}
                        if obj[1]>9:
                           return 'liver'
                        elif obj[1]<=9:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[6]>54:
                     # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[1]>12:
                        return 'liver'
                     elif obj[1]<=12:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[8]>9:
               # {"feature": "Alamine_Aminotransferase", "instances": 17, "metric_value": 0.0, "depth": 5}
               if obj[4]<=43:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 13, "metric_value": -0.0, "depth": 6}
                  if obj[5]>27:
                     # {"feature": "Total_Protiens", "instances": 8, "metric_value": -0.0, "depth": 7}
                     if obj[6]>57:
                        # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[1]>7:
                           return 'liver'
                        elif obj[1]<=7:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[6]<=57:
                        # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=8:
                           return 'normal'
                        elif obj[1]>8:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[5]<=27:
                     # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Total_Protiens", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[6]>55:
                           return 'liver'
                        elif obj[6]<=55:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]<=1:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[4]>43:
                  # {"feature": "Total_Protiens", "instances": 4, "metric_value": 0.0, "depth": 6}
                  if obj[6]>69:
                     # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=8:
                        return 'normal'
                     elif obj[1]>8:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[6]<=69:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 25, "metric_value": -0.0, "depth": 4}
            if obj[8]<=7:
               # {"feature": "Direct_Bilirubin", "instances": 16, "metric_value": 0.0, "depth": 5}
               if obj[2]>6:
                  # {"feature": "Total_Bilirubin", "instances": 10, "metric_value": -0.0, "depth": 6}
                  if obj[1]>27:
                     # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[4]>50:
                        return 'liver'
                     elif obj[4]<=50:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": -0.0, "depth": 8}
                        if obj[5]>47:
                           return 'liver'
                        elif obj[5]<=47:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[1]<=27:
                     # {"feature": "Total_Protiens", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[6]<=6:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=10:
                           return 'normal'
                        elif obj[4]>10:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[6]>6:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[2]<=6:
                  # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=9:
                     # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=30:
                        # {"feature": "Total_Protiens", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[6]<=8:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>30:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>9:
                     # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": -0.0, "depth": 7}
                     if obj[4]>28:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[5]>92:
                           return 'normal'
                        elif obj[5]<=92:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=28:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[8]>7:
               # {"feature": "Total_Bilirubin", "instances": 9, "metric_value": 0.0, "depth": 5}
               if obj[1]<=21:
                  return 'liver'
               elif obj[1]>21:
                  # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=12:
                     return 'normal'
                  elif obj[2]>12:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'normal'
            else:
               return 'liver'
         else:
            return 'liver'
      else:
         return 'liver'
   else:
      return 'liver'
