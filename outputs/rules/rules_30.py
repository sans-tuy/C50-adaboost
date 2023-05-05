def findDecision(obj): #obj[0]: Age, obj[1]: Total_Bilirubin, obj[2]: Direct_Bilirubin, obj[3]: Alkaline_Phosphotase, obj[4]: Alamine_Aminotransferase, obj[5]: Aspartate_Aminotransferase, obj[6]: Total_Protiens, obj[7]: Albumin, obj[8]: Albumin_and_Globulin_Ratio
   # {"feature": "Age", "instances": 519, "metric_value": 0.0, "depth": 1}
   if obj[0]>44.323699421965316:
      # {"feature": "Albumin", "instances": 270, "metric_value": 0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Alkaline_Phosphotase", "instances": 152, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Direct_Bilirubin", "instances": 117, "metric_value": 0.0, "depth": 4}
            if obj[2]<=7:
               # {"feature": "Total_Bilirubin", "instances": 96, "metric_value": -0.0, "depth": 5}
               if obj[1]<=8:
                  # {"feature": "Total_Protiens", "instances": 62, "metric_value": -0.0, "depth": 6}
                  if obj[6]>63.564516129032256:
                     # {"feature": "Alamine_Aminotransferase", "instances": 40, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=30.925:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 25, "metric_value": 0.0, "depth": 8}
                        if obj[8]<=14:
                           return 'liver'
                        elif obj[8]>14:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]>30.925:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 15, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=70:
                           return 'liver'
                        elif obj[5]>70:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[6]<=63.564516129032256:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 22, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=29:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 15, "metric_value": -0.0, "depth": 8}
                        if obj[8]>9:
                           return 'normal'
                        elif obj[8]<=9:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]>29:
                        # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=51:
                           return 'liver'
                        elif obj[4]>51:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[1]>8:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 34, "metric_value": 0.0, "depth": 6}
                  if obj[8]<=166:
                     # {"feature": "Total_Protiens", "instances": 33, "metric_value": -0.0, "depth": 7}
                     if obj[6]<=67:
                        # {"feature": "Alamine_Aminotransferase", "instances": 20, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=45:
                           return 'liver'
                        elif obj[4]>45:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[6]>67:
                        # {"feature": "Alamine_Aminotransferase", "instances": 13, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=38:
                           return 'liver'
                        elif obj[4]>38:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]>166:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[2]>7:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 21, "metric_value": 0.0, "depth": 5}
               if obj[8]<=14:
                  # {"feature": "Total_Bilirubin", "instances": 17, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=35:
                     # {"feature": "Total_Protiens", "instances": 13, "metric_value": -0.0, "depth": 7}
                     if obj[6]<=65:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 9, "metric_value": -0.0, "depth": 8}
                        if obj[5]>40:
                           return 'liver'
                        elif obj[5]<=40:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[6]>65:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>35:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[8]>14:
                  # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=16:
                     # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[4]>18:
                        return 'normal'
                     elif obj[4]<=18:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>16:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Total_Protiens", "instances": 35, "metric_value": -0.0, "depth": 4}
            if obj[6]>62:
               # {"feature": "Alamine_Aminotransferase", "instances": 22, "metric_value": -0.0, "depth": 5}
               if obj[4]>24:
                  return 'liver'
               elif obj[4]<=24:
                  return 'normal'
               else:
                  return 'normal'
            elif obj[6]<=62:
               return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      elif obj[7]<=26.393063583815028:
         # {"feature": "Alkaline_Phosphotase", "instances": 118, "metric_value": -0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Aspartate_Aminotransferase", "instances": 81, "metric_value": 0.0, "depth": 4}
            if obj[5]<=70.09876543209876:
               # {"feature": "Alamine_Aminotransferase", "instances": 59, "metric_value": 0.0, "depth": 5}
               if obj[4]>10:
                  # {"feature": "Total_Bilirubin", "instances": 58, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=16.775862068965516:
                     # {"feature": "Total_Protiens", "instances": 39, "metric_value": 0.0, "depth": 7}
                     if obj[6]>21.958985274941274:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 30, "metric_value": 0.0, "depth": 8}
                        if obj[8]<=9:
                           return 'liver'
                        elif obj[8]>9:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[6]<=21.958985274941274:
                        # {"feature": "Direct_Bilirubin", "instances": 9, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>16.775862068965516:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 19, "metric_value": -0.0, "depth": 7}
                     if obj[8]<=7:
                        # {"feature": "Direct_Bilirubin", "instances": 15, "metric_value": -0.0, "depth": 8}
                        if obj[2]>2:
                           return 'liver'
                        elif obj[2]<=2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]>7:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[4]<=10:
                  return 'normal'
               else:
                  return 'normal'
            elif obj[5]>70.09876543209876:
               # {"feature": "Total_Bilirubin", "instances": 22, "metric_value": -0.0, "depth": 5}
               if obj[1]<=184:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 21, "metric_value": -0.0, "depth": 6}
                  if obj[8]>6:
                     # {"feature": "Alamine_Aminotransferase", "instances": 12, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=46:
                        # {"feature": "Direct_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]>46:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]<=6:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[1]>184:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 37, "metric_value": -0.0, "depth": 4}
            if obj[8]<=8:
               # {"feature": "Total_Bilirubin", "instances": 28, "metric_value": -0.0, "depth": 5}
               if obj[1]<=72.71428571428571:
                  return 'liver'
               elif obj[1]>72.71428571428571:
                  # {"feature": "Alamine_Aminotransferase", "instances": 11, "metric_value": 0.0, "depth": 6}
                  if obj[4]<=173:
                     # {"feature": "Total_Protiens", "instances": 7, "metric_value": -0.0, "depth": 7}
                     if obj[6]<=61:
                        # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[2]>5:
                           return 'liver'
                        elif obj[2]<=5:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[6]>61:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]>173:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[8]>8:
               # {"feature": "Direct_Bilirubin", "instances": 9, "metric_value": 0.0, "depth": 5}
               if obj[2]>1:
                  # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 6}
                  if obj[4]>16:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[5]>25:
                        # {"feature": "Total_Protiens", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[6]>6:
                           return 'liver'
                        elif obj[6]<=6:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=25:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=16:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[2]<=1:
                  # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 6}
                  if obj[1]>5:
                     return 'liver'
                  elif obj[1]<=5:
                     return 'normal'
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
   elif obj[0]<=44.323699421965316:
      # {"feature": "Albumin", "instances": 249, "metric_value": 0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Total_Protiens", "instances": 154, "metric_value": 0.0, "depth": 3}
         if obj[6]>63.0:
            # {"feature": "Alkaline_Phosphotase", "instances": 110, "metric_value": -0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Direct_Bilirubin", "instances": 78, "metric_value": 0.0, "depth": 5}
               if obj[2]>1:
                  # {"feature": "Alamine_Aminotransferase", "instances": 70, "metric_value": -0.0, "depth": 6}
                  if obj[4]<=62.91428571428571:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 60, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=76.34543098134603:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 53, "metric_value": -0.0, "depth": 8}
                        if obj[8]<=17:
                           return 'normal'
                        elif obj[8]>17:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>76.34543098134603:
                        # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=8:
                           return 'normal'
                        elif obj[1]>8:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[4]>62.91428571428571:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[2]<=1:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 6}
                  if obj[5]>19:
                     # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=32:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 4, "metric_value": -0.0, "depth": 8}
                        if obj[8]<=1:
                           return 'liver'
                        elif obj[8]>1:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]>32:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=6:
                           return 'normal'
                        elif obj[1]>6:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[5]<=19:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[3]>291.0539499036609:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 32, "metric_value": 0.0, "depth": 5}
               if obj[8]<=18:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 31, "metric_value": -0.0, "depth": 6}
                  if obj[5]<=198.6451612903226:
                     # {"feature": "Alamine_Aminotransferase", "instances": 21, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=74:
                        # {"feature": "Total_Bilirubin", "instances": 16, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=8:
                           return 'normal'
                        elif obj[1]>8:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>74:
                        # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[5]>198.6451612903226:
                     # {"feature": "Alamine_Aminotransferase", "instances": 10, "metric_value": -0.0, "depth": 7}
                     if obj[4]>68:
                        # {"feature": "Total_Bilirubin", "instances": 9, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=39:
                           return 'liver'
                        elif obj[1]>39:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=68:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[8]>18:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[6]<=63.0:
            # {"feature": "Direct_Bilirubin", "instances": 44, "metric_value": 0.0, "depth": 4}
            if obj[2]>1:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 36, "metric_value": -0.0, "depth": 5}
               if obj[8]<=9:
                  # {"feature": "Alamine_Aminotransferase", "instances": 21, "metric_value": -0.0, "depth": 6}
                  if obj[4]>15:
                     # {"feature": "Total_Bilirubin", "instances": 19, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=67:
                        # {"feature": "Alkaline_Phosphotase", "instances": 15, "metric_value": -0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'liver'
                        elif obj[3]>291.0539499036609:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>67:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=15:
                     # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=6:
                        return 'normal'
                     elif obj[1]>6:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               elif obj[8]>9:
                  # {"feature": "Alkaline_Phosphotase", "instances": 15, "metric_value": -0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Alamine_Aminotransferase", "instances": 14, "metric_value": -0.0, "depth": 7}
                     if obj[4]>19:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 12, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=190:
                           return 'liver'
                        elif obj[5]>190:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=19:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[3]>291.0539499036609:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[2]<=1:
               # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": -0.0, "depth": 5}
               if obj[1]<=6:
                  # {"feature": "Alkaline_Phosphotase", "instances": 5, "metric_value": 0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[4]>22:
                        return 'liver'
                     elif obj[4]<=22:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[1]>6:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[5]<=34:
                     # {"feature": "Alkaline_Phosphotase", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        return 'liver'
                     elif obj[3]>291.0539499036609:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[5]>34:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'normal'
            else:
               return 'liver'
         else:
            return 'liver'
      elif obj[7]<=26.393063583815028:
         # {"feature": "Alkaline_Phosphotase", "instances": 95, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 70, "metric_value": -0.0, "depth": 4}
            if obj[8]<=9:
               # {"feature": "Total_Protiens", "instances": 53, "metric_value": -0.0, "depth": 5}
               if obj[6]>14.72764200252426:
                  # {"feature": "Total_Bilirubin", "instances": 35, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=17:
                     # {"feature": "Alamine_Aminotransferase", "instances": 23, "metric_value": -0.0, "depth": 7}
                     if obj[4]>22:
                        # {"feature": "Direct_Bilirubin", "instances": 14, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]<=22:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 9, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=22:
                           return 'normal'
                        elif obj[5]>22:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  elif obj[1]>17:
                     # {"feature": "Alamine_Aminotransferase", "instances": 12, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=65:
                        # {"feature": "Direct_Bilirubin", "instances": 9, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=45:
                           return 'liver'
                        elif obj[2]>45:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>65:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[6]<=14.72764200252426:
                  # {"feature": "Direct_Bilirubin", "instances": 18, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=4:
                     # {"feature": "Alamine_Aminotransferase", "instances": 14, "metric_value": -0.0, "depth": 7}
                     if obj[4]>12:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 13, "metric_value": -0.0, "depth": 8}
                        if obj[5]>23:
                           return 'liver'
                        elif obj[5]<=23:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=12:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]>4:
                     # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[1]>13:
                        # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[4]>25:
                           return 'liver'
                        elif obj[4]<=25:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=13:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[8]>9:
               # {"feature": "Aspartate_Aminotransferase", "instances": 17, "metric_value": -0.0, "depth": 5}
               if obj[5]<=32:
                  # {"feature": "Alamine_Aminotransferase", "instances": 11, "metric_value": -0.0, "depth": 6}
                  if obj[4]<=27:
                     # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": -0.0, "depth": 7}
                     if obj[1]>6:
                        # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        elif obj[2]>2:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]<=6:
                        # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]>27:
                     # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=2:
                        # {"feature": "Total_Protiens", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[6]>7:
                           return 'normal'
                        elif obj[6]<=7:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               elif obj[5]>32:
                  # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 6}
                  if obj[4]>22:
                     # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[1]>2:
                        # {"feature": "Total_Protiens", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[6]>69:
                           return 'normal'
                        elif obj[6]<=69:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=2:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=22:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Direct_Bilirubin", "instances": 25, "metric_value": 0.0, "depth": 4}
            if obj[2]<=82:
               # {"feature": "Alamine_Aminotransferase", "instances": 22, "metric_value": -0.0, "depth": 5}
               if obj[4]<=48:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 12, "metric_value": -0.0, "depth": 6}
                  if obj[8]>5:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[5]<=40:
                        return 'liver'
                     elif obj[5]>40:
                        # {"feature": "Total_Protiens", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[6]>59:
                           return 'normal'
                        elif obj[6]<=59:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]<=5:
                     # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[1]>9:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=21:
                           return 'normal'
                        elif obj[5]>21:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=9:
                        # {"feature": "Total_Protiens", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[6]<=8:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'normal'
               elif obj[4]>48:
                  # {"feature": "Total_Protiens", "instances": 10, "metric_value": 0.0, "depth": 6}
                  if obj[6]>8:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 7, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=86:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[8]>7:
                           return 'normal'
                        elif obj[8]<=7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>86:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[6]<=8:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[8]<=1:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[5]>48:
                           return 'liver'
                        elif obj[5]<=48:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[2]>82:
               return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      else:
         return 'liver'
   else:
      return 'liver'
