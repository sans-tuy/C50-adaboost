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
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 64, "metric_value": 0.0, "depth": 6}
                  if obj[8]<=15:
                     # {"feature": "Alamine_Aminotransferase", "instances": 60, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=27.816666666666666:
                        # {"feature": "Total_Bilirubin", "instances": 36, "metric_value": 0.0, "depth": 8}
                        if obj[1]>1:
                           return 'liver'
                        elif obj[1]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>27.816666666666666:
                        # {"feature": "Total_Bilirubin", "instances": 24, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=23:
                           return 'liver'
                        elif obj[1]>23:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]>15:
                     # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=2:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]>8:
                           return 'liver'
                        elif obj[1]<=8:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]>2:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               elif obj[6]<=60.08139534883721:
                  # {"feature": "Alamine_Aminotransferase", "instances": 22, "metric_value": -0.0, "depth": 6}
                  if obj[4]>12:
                     # {"feature": "Direct_Bilirubin", "instances": 21, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=5:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 18, "metric_value": -0.0, "depth": 8}
                        if obj[8]<=139:
                           return 'normal'
                        elif obj[8]>139:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]>5:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=12:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'normal'
            elif obj[5]>54.30769230769231:
               # {"feature": "Alamine_Aminotransferase", "instances": 31, "metric_value": -0.0, "depth": 5}
               if obj[4]<=79.90322580645162:
                  # {"feature": "Total_Protiens", "instances": 19, "metric_value": 0.0, "depth": 6}
                  if obj[6]<=65:
                     # {"feature": "Direct_Bilirubin", "instances": 11, "metric_value": -0.0, "depth": 7}
                     if obj[2]>2:
                        # {"feature": "Total_Bilirubin", "instances": 9, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=94:
                           return 'liver'
                        elif obj[1]>94:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]<=2:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=6:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[6]>65:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[8]>1:
                        # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=5:
                           return 'normal'
                        elif obj[2]>5:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[8]<=1:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[4]>79.90322580645162:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Total_Bilirubin", "instances": 35, "metric_value": 0.0, "depth": 4}
            if obj[1]<=61.628571428571426:
               # {"feature": "Total_Protiens", "instances": 23, "metric_value": 0.0, "depth": 5}
               if obj[6]<=71:
                  return 'liver'
               elif obj[6]>71:
                  # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": -0.0, "depth": 6}
                  if obj[4]>24:
                     return 'liver'
                  elif obj[4]<=24:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[1]>61.628571428571426:
               return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      elif obj[7]<=26.393063583815028:
         # {"feature": "Alkaline_Phosphotase", "instances": 118, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Total_Bilirubin", "instances": 81, "metric_value": 0.0, "depth": 4}
            if obj[1]>1:
               # {"feature": "Total_Protiens", "instances": 77, "metric_value": 0.0, "depth": 5}
               if obj[6]<=70.1873311645709:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 65, "metric_value": -0.0, "depth": 6}
                  if obj[8]<=9:
                     # {"feature": "Alamine_Aminotransferase", "instances": 51, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=41.333333333333336:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 33, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=60.02711625633464:
                           return 'liver'
                        elif obj[5]>60.02711625633464:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>41.333333333333336:
                        # {"feature": "Direct_Bilirubin", "instances": 18, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=88:
                           return 'liver'
                        elif obj[2]>88:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]>9:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 14, "metric_value": 0.0, "depth": 7}
                     if obj[5]>23:
                        # {"feature": "Alamine_Aminotransferase", "instances": 11, "metric_value": -0.0, "depth": 8}
                        if obj[4]>30:
                           return 'liver'
                        elif obj[4]<=30:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=23:
                        # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
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
               elif obj[6]>70.1873311645709:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[1]<=1:
               # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 5}
               if obj[2]<=3:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 6}
                  if obj[5]>13:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[8]>1:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=22:
                           return 'normal'
                        elif obj[4]>22:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]<=1:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[5]<=13:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'normal'
            else:
               return 'normal'
         elif obj[3]>291.0539499036609:
            # {"feature": "Direct_Bilirubin", "instances": 37, "metric_value": 0.0, "depth": 4}
            if obj[2]<=29.27027027027027:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 24, "metric_value": 0.0, "depth": 5}
               if obj[8]<=55:
                  # {"feature": "Total_Bilirubin", "instances": 23, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=19:
                     # {"feature": "Total_Protiens", "instances": 12, "metric_value": -0.0, "depth": 7}
                     if obj[6]>53:
                        # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[4]>20:
                           return 'liver'
                        elif obj[4]<=20:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[6]<=53:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>19:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[8]>55:
                  return 'normal'
               else:
                  return 'normal'
            elif obj[2]>29.27027027027027:
               # {"feature": "Total_Protiens", "instances": 13, "metric_value": -0.0, "depth": 5}
               if obj[6]>55:
                  # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": -0.0, "depth": 6}
                  if obj[1]>68:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 7, "metric_value": -0.0, "depth": 7}
                     if obj[8]<=4:
                        return 'liver'
                     elif obj[8]>4:
                        # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[4]>48:
                           return 'liver'
                        elif obj[4]<=48:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=68:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[6]<=55:
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
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 116, "metric_value": 0.0, "depth": 4}
            if obj[8]<=152.65271437127222:
               # {"feature": "Total_Bilirubin", "instances": 113, "metric_value": 0.0, "depth": 5}
               if obj[1]<=177.07189571631957:
                  # {"feature": "Direct_Bilirubin", "instances": 110, "metric_value": -0.0, "depth": 6}
                  if obj[2]>1:
                     # {"feature": "Total_Protiens", "instances": 95, "metric_value": -0.0, "depth": 7}
                     if obj[6]>61.04210526315789:
                        # {"feature": "Alamine_Aminotransferase", "instances": 71, "metric_value": 0.0, "depth": 8}
                        if obj[4]>11:
                           return 'liver'
                        elif obj[4]<=11:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[6]<=61.04210526315789:
                        # {"feature": "Alamine_Aminotransferase", "instances": 24, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=325.5416666666667:
                           return 'liver'
                        elif obj[4]>325.5416666666667:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]<=1:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 15, "metric_value": -0.0, "depth": 7}
                     if obj[5]>19:
                        # {"feature": "Total_Protiens", "instances": 14, "metric_value": -0.0, "depth": 8}
                        if obj[6]<=72:
                           return 'liver'
                        elif obj[6]>72:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=19:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[1]>177.07189571631957:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[8]>152.65271437127222:
               # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 5}
               if obj[4]>36:
                  # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=1:
                     return 'normal'
                  elif obj[1]>1:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[4]<=36:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Total_Protiens", "instances": 38, "metric_value": -0.0, "depth": 4}
            if obj[6]>69:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 21, "metric_value": -0.0, "depth": 5}
               if obj[8]>1:
                  # {"feature": "Total_Bilirubin", "instances": 15, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=15:
                     # {"feature": "Alamine_Aminotransferase", "instances": 10, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=28:
                        # {"feature": "Direct_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=1:
                           return 'normal'
                        elif obj[2]>1:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>28:
                        # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=3:
                           return 'liver'
                        elif obj[2]>3:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>15:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[8]<=1:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": -0.0, "depth": 6}
                  if obj[5]>42:
                     # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=15:
                        # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": -0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]>15:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]<=42:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'normal'
            elif obj[6]<=69:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 17, "metric_value": -0.0, "depth": 5}
               if obj[8]<=13:
                  # {"feature": "Alamine_Aminotransferase", "instances": 15, "metric_value": -0.0, "depth": 6}
                  if obj[4]<=102:
                     # {"feature": "Direct_Bilirubin", "instances": 8, "metric_value": -0.0, "depth": 7}
                     if obj[2]>2:
                        # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[1]>9:
                           return 'liver'
                        elif obj[1]<=9:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]<=2:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=8:
                           return 'liver'
                        elif obj[1]>8:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[4]>102:
                     # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=9:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[5]>231:
                           return 'liver'
                        elif obj[5]<=231:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]>9:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[8]>13:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      elif obj[7]<=26.393063583815028:
         # {"feature": "Albumin_and_Globulin_Ratio", "instances": 95, "metric_value": 0.0, "depth": 3}
         if obj[8]>1:
            # {"feature": "Alkaline_Phosphotase", "instances": 75, "metric_value": 0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Total_Protiens", "instances": 55, "metric_value": 0.0, "depth": 5}
               if obj[6]>7.618831448305244:
                  # {"feature": "Alamine_Aminotransferase", "instances": 47, "metric_value": -0.0, "depth": 6}
                  if obj[4]>11:
                     # {"feature": "Direct_Bilirubin", "instances": 46, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=4:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 31, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=119.11937373855483:
                           return 'normal'
                        elif obj[5]>119.11937373855483:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>4:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 15, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=130:
                           return 'liver'
                        elif obj[5]>130:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=11:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[6]<=7.618831448305244:
                  # {"feature": "Alamine_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 6}
                  if obj[4]>25:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": -0.0, "depth": 7}
                     if obj[5]>32:
                        # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": -0.0, "depth": 8}
                        if obj[1]>8:
                           return 'liver'
                        elif obj[1]<=8:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]<=32:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[4]<=25:
                     # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[1]>7:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=7:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[3]>291.0539499036609:
               # {"feature": "Alamine_Aminotransferase", "instances": 20, "metric_value": 0.0, "depth": 5}
               if obj[4]<=52:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 13, "metric_value": -0.0, "depth": 6}
                  if obj[5]>21:
                     # {"feature": "Direct_Bilirubin", "instances": 12, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=36:
                        # {"feature": "Total_Protiens", "instances": 11, "metric_value": -0.0, "depth": 8}
                        if obj[6]<=61:
                           return 'liver'
                        elif obj[6]>61:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>36:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]<=21:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[4]>52:
                  # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 6}
                  if obj[2]>2:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[5]>57:
                        return 'liver'
                     elif obj[5]<=57:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[2]<=2:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[8]<=1:
            # {"feature": "Total_Bilirubin", "instances": 20, "metric_value": 0.0, "depth": 4}
            if obj[1]<=13:
               # {"feature": "Aspartate_Aminotransferase", "instances": 13, "metric_value": 0.0, "depth": 5}
               if obj[5]<=34:
                  # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=2:
                     # {"feature": "Total_Protiens", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[6]>6:
                        # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[4]>26:
                           return 'liver'
                        elif obj[4]<=26:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[6]<=6:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]>2:
                     # {"feature": "Alkaline_Phosphotase", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Total_Protiens", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[6]<=8:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[5]>34:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[1]>13:
               # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": -0.0, "depth": 5}
               if obj[2]<=8:
                  # {"feature": "Alkaline_Phosphotase", "instances": 4, "metric_value": 0.0, "depth": 6}
                  if obj[3]>291.0539499036609:
                     # {"feature": "Total_Protiens", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[6]<=6:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=60:
                           return 'normal'
                        elif obj[4]>60:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  elif obj[3]<=291.0539499036609:
                     # {"feature": "Total_Protiens", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[6]<=8:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]>25:
                           return 'normal'
                        elif obj[4]<=25:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               elif obj[2]>8:
                  # {"feature": "Alkaline_Phosphotase", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     return 'normal'
                  elif obj[3]>291.0539499036609:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'normal'
            else:
               return 'normal'
         else:
            return 'liver'
      else:
         return 'liver'
   else:
      return 'liver'
