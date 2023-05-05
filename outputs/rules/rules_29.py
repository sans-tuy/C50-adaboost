def findDecision(obj): #obj[0]: Age, obj[1]: Total_Bilirubin, obj[2]: Direct_Bilirubin, obj[3]: Alkaline_Phosphotase, obj[4]: Alamine_Aminotransferase, obj[5]: Aspartate_Aminotransferase, obj[6]: Total_Protiens, obj[7]: Albumin, obj[8]: Albumin_and_Globulin_Ratio
   # {"feature": "Age", "instances": 519, "metric_value": 0.0, "depth": 1}
   if obj[0]>44.323699421965316:
      # {"feature": "Albumin", "instances": 270, "metric_value": 0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Alkaline_Phosphotase", "instances": 152, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Alamine_Aminotransferase", "instances": 117, "metric_value": 0.0, "depth": 4}
            if obj[4]>10:
               # {"feature": "Total_Bilirubin", "instances": 116, "metric_value": 0.0, "depth": 5}
               if obj[1]<=12.956896551724139:
                  # {"feature": "Direct_Bilirubin", "instances": 90, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=2:
                     # {"feature": "Total_Protiens", "instances": 63, "metric_value": -0.0, "depth": 7}
                     if obj[6]>60.666666666666664:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 47, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=31.638297872340427:
                           return 'liver'
                        elif obj[5]>31.638297872340427:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[6]<=60.666666666666664:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 16, "metric_value": 0.0, "depth": 8}
                        if obj[5]>12:
                           return 'liver'
                        elif obj[5]<=12:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[2]>2:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 27, "metric_value": 0.0, "depth": 7}
                     if obj[8]<=111:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 25, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=73:
                           return 'liver'
                        elif obj[5]>73:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]>111:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=24:
                           return 'normal'
                        elif obj[5]>24:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[1]>12.956896551724139:
                  # {"feature": "Direct_Bilirubin", "instances": 26, "metric_value": -0.0, "depth": 6}
                  if obj[2]>4:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 23, "metric_value": -0.0, "depth": 7}
                     if obj[8]<=15:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 19, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=84:
                           return 'liver'
                        elif obj[5]>84:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]>15:
                        # {"feature": "Total_Protiens", "instances": 4, "metric_value": -0.0, "depth": 8}
                        if obj[6]>59:
                           return 'normal'
                        elif obj[6]<=59:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]<=4:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 3, "metric_value": -0.0, "depth": 7}
                     if obj[8]>9:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=25:
                           return 'normal'
                        elif obj[5]>25:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]<=9:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[4]<=10:
               return 'normal'
            else:
               return 'normal'
         elif obj[3]>291.0539499036609:
            # {"feature": "Direct_Bilirubin", "instances": 35, "metric_value": 0.0, "depth": 4}
            if obj[2]<=27.542857142857144:
               # {"feature": "Total_Bilirubin", "instances": 25, "metric_value": 0.0, "depth": 5}
               if obj[1]>6:
                  # {"feature": "Total_Protiens", "instances": 24, "metric_value": 0.0, "depth": 6}
                  if obj[6]>62:
                     # {"feature": "Alamine_Aminotransferase", "instances": 13, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=110:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 11, "metric_value": -0.0, "depth": 8}
                        if obj[5]>17:
                           return 'liver'
                        elif obj[5]<=17:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>110:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[6]<=62:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[1]<=6:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[2]>27.542857142857144:
               return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      elif obj[7]<=26.393063583815028:
         # {"feature": "Alkaline_Phosphotase", "instances": 118, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Aspartate_Aminotransferase", "instances": 81, "metric_value": 0.0, "depth": 4}
            if obj[5]>12:
               # {"feature": "Total_Protiens", "instances": 80, "metric_value": 0.0, "depth": 5}
               if obj[6]>47.1:
                  # {"feature": "Total_Bilirubin", "instances": 53, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=31.264150943396228:
                     # {"feature": "Direct_Bilirubin", "instances": 41, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=4:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 25, "metric_value": -0.0, "depth": 8}
                        if obj[8]>6:
                           return 'liver'
                        elif obj[8]<=6:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>4:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 16, "metric_value": 0.0, "depth": 8}
                        if obj[8]<=11:
                           return 'liver'
                        elif obj[8]>11:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>31.264150943396228:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[6]<=47.1:
                  # {"feature": "Alamine_Aminotransferase", "instances": 27, "metric_value": -0.0, "depth": 6}
                  if obj[4]<=45.77777777777778:
                     # {"feature": "Direct_Bilirubin", "instances": 19, "metric_value": 0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 17, "metric_value": 0.0, "depth": 8}
                        if obj[8]<=7:
                           return 'liver'
                        elif obj[8]>7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]<=1:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]>6:
                           return 'normal'
                        elif obj[1]<=6:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  elif obj[4]>45.77777777777778:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[5]<=12:
               return 'normal'
            else:
               return 'normal'
         elif obj[3]>291.0539499036609:
            # {"feature": "Direct_Bilirubin", "instances": 37, "metric_value": 0.0, "depth": 4}
            if obj[2]>1:
               # {"feature": "Total_Bilirubin", "instances": 33, "metric_value": 0.0, "depth": 5}
               if obj[1]<=68.87878787878788:
                  # {"feature": "Alamine_Aminotransferase", "instances": 21, "metric_value": 0.0, "depth": 6}
                  if obj[4]>52:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 12, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=141:
                        return 'liver'
                     elif obj[5]>141:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[8]<=7:
                           return 'liver'
                        elif obj[8]>7:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[4]<=52:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[1]>68.87878787878788:
                  # {"feature": "Alamine_Aminotransferase", "instances": 12, "metric_value": -0.0, "depth": 6}
                  if obj[4]>35:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 11, "metric_value": -0.0, "depth": 7}
                     if obj[5]>57:
                        # {"feature": "Total_Protiens", "instances": 8, "metric_value": -0.0, "depth": 8}
                        if obj[6]>65:
                           return 'liver'
                        elif obj[6]<=65:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=57:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=35:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[2]<=1:
               # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 5}
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
   elif obj[0]<=44.323699421965316:
      # {"feature": "Albumin", "instances": 249, "metric_value": 0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Total_Protiens", "instances": 154, "metric_value": 0.0, "depth": 3}
         if obj[6]>63.0:
            # {"feature": "Alkaline_Phosphotase", "instances": 110, "metric_value": 0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 78, "metric_value": -0.0, "depth": 5}
               if obj[8]<=31.05128205128205:
                  # {"feature": "Alamine_Aminotransferase", "instances": 64, "metric_value": 0.0, "depth": 6}
                  if obj[4]<=55.015625:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 53, "metric_value": 0.0, "depth": 7}
                     if obj[5]>11:
                        # {"feature": "Total_Bilirubin", "instances": 52, "metric_value": -0.0, "depth": 8}
                        if obj[1]>7:
                           return 'normal'
                        elif obj[1]<=7:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]<=11:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]>55.015625:
                     # {"feature": "Total_Bilirubin", "instances": 11, "metric_value": -0.0, "depth": 7}
                     if obj[1]>9:
                        return 'liver'
                     elif obj[1]<=9:
                        # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
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
               elif obj[8]>31.05128205128205:
                  # {"feature": "Total_Bilirubin", "instances": 14, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=16:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 9, "metric_value": -0.0, "depth": 7}
                     if obj[5]>36:
                        # {"feature": "Direct_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=3:
                           return 'liver'
                        elif obj[2]>3:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=36:
                        # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'normal'
                        elif obj[2]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  elif obj[1]>16:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[3]>291.0539499036609:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 32, "metric_value": 0.0, "depth": 5}
               if obj[8]>7:
                  # {"feature": "Alamine_Aminotransferase", "instances": 22, "metric_value": -0.0, "depth": 6}
                  if obj[4]<=68:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 12, "metric_value": 0.0, "depth": 7}
                     if obj[5]<=58:
                        # {"feature": "Direct_Bilirubin", "instances": 9, "metric_value": -0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]>58:
                        # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]>68:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 10, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=275:
                        # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": -0.0, "depth": 8}
                        if obj[1]<=21:
                           return 'liver'
                        elif obj[1]>21:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>275:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[8]<=7:
                  # {"feature": "Total_Bilirubin", "instances": 10, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=19:
                     # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": -0.0, "depth": 7}
                     if obj[2]>2:
                        # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[4]>21:
                           return 'liver'
                        elif obj[4]<=21:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]<=2:
                        # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[4]>28:
                           return 'liver'
                        elif obj[4]<=28:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[1]>19:
                     # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]>28:
                           return 'liver'
                        elif obj[4]<=28:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]<=1:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[6]<=63.0:
            # {"feature": "Alkaline_Phosphotase", "instances": 44, "metric_value": -0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 38, "metric_value": 0.0, "depth": 5}
               if obj[8]<=11:
                  # {"feature": "Total_Bilirubin", "instances": 26, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=71:
                     # {"feature": "Direct_Bilirubin", "instances": 23, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=3:
                        # {"feature": "Alamine_Aminotransferase", "instances": 16, "metric_value": 0.0, "depth": 8}
                        if obj[4]>21:
                           return 'liver'
                        elif obj[4]<=21:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]>3:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 7, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=113:
                           return 'liver'
                        elif obj[5]>113:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>71:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[8]>11:
                  # {"feature": "Alamine_Aminotransferase", "instances": 12, "metric_value": -0.0, "depth": 6}
                  if obj[4]>19:
                     # {"feature": "Direct_Bilirubin", "instances": 11, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=2:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 7, "metric_value": -0.0, "depth": 8}
                        if obj[5]>30:
                           return 'liver'
                        elif obj[5]<=30:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]>2:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=19:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[3]>291.0539499036609:
               # {"feature": "Direct_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 5}
               if obj[2]<=3:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 4, "metric_value": 0.0, "depth": 6}
                  if obj[8]>1:
                     # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=25:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=8:
                           return 'liver'
                        elif obj[1]>8:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[8]<=1:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[2]>3:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      elif obj[7]<=26.393063583815028:
         # {"feature": "Alkaline_Phosphotase", "instances": 95, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 70, "metric_value": 0.0, "depth": 4}
            if obj[8]<=95:
               # {"feature": "Total_Protiens", "instances": 68, "metric_value": -0.0, "depth": 5}
               if obj[6]>43.794117647058826:
                  # {"feature": "Total_Bilirubin", "instances": 44, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=77:
                     # {"feature": "Direct_Bilirubin", "instances": 37, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=2:
                        # {"feature": "Alamine_Aminotransferase", "instances": 27, "metric_value": -0.0, "depth": 8}
                        if obj[4]>11:
                           return 'liver'
                        elif obj[4]<=11:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]>2:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 10, "metric_value": 0.0, "depth": 8}
                        if obj[5]>27:
                           return 'liver'
                        elif obj[5]<=27:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[1]>77:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[6]<=43.794117647058826:
                  # {"feature": "Alamine_Aminotransferase", "instances": 24, "metric_value": 0.0, "depth": 6}
                  if obj[4]>23:
                     # {"feature": "Direct_Bilirubin", "instances": 15, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=3:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 10, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=28:
                           return 'liver'
                        elif obj[5]>28:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]>3:
                        # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[1]>13:
                           return 'liver'
                        elif obj[1]<=13:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=23:
                     # {"feature": "Direct_Bilirubin", "instances": 9, "metric_value": -0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[1]>8:
                           return 'normal'
                        elif obj[1]<=8:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]<=1:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[8]>95:
               # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 5}
               if obj[1]>2:
                  return 'normal'
               elif obj[1]<=2:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'normal'
         elif obj[3]>291.0539499036609:
            # {"feature": "Total_Protiens", "instances": 25, "metric_value": 0.0, "depth": 4}
            if obj[6]>54:
               # {"feature": "Alamine_Aminotransferase", "instances": 14, "metric_value": -0.0, "depth": 5}
               if obj[4]>41:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 6}
                  if obj[5]<=88:
                     # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[1]>8:
                        # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=12:
                           return 'normal'
                        elif obj[2]>12:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=8:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]>88:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[4]<=41:
                  # {"feature": "Direct_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 6}
                  if obj[2]>13:
                     # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[1]>25:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=47:
                           return 'normal'
                        elif obj[5]>47:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=25:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]<=13:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[6]<=54:
               # {"feature": "Alamine_Aminotransferase", "instances": 11, "metric_value": 0.0, "depth": 5}
               if obj[4]>28:
                  # {"feature": "Total_Bilirubin", "instances": 9, "metric_value": 0.0, "depth": 6}
                  if obj[1]>9:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[8]>1:
                        return 'liver'
                     elif obj[8]<=1:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[5]>48:
                           return 'liver'
                        elif obj[5]<=48:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=9:
                     # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=2:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=17:
                           return 'liver'
                        elif obj[5]>17:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]>2:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[4]<=28:
                  # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 6}
                  if obj[1]>12:
                     return 'normal'
                  elif obj[1]<=12:
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
