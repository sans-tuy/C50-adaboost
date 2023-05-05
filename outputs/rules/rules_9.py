def findDecision(obj): #obj[0]: Age, obj[1]: Total_Bilirubin, obj[2]: Direct_Bilirubin, obj[3]: Alkaline_Phosphotase, obj[4]: Alamine_Aminotransferase, obj[5]: Aspartate_Aminotransferase, obj[6]: Total_Protiens, obj[7]: Albumin, obj[8]: Albumin_and_Globulin_Ratio
   # {"feature": "Albumin", "instances": 519, "metric_value": 0.0, "depth": 1}
   if obj[7]>26.393063583815028:
      # {"feature": "Age", "instances": 306, "metric_value": -0.0, "depth": 2}
      if obj[0]>43.12091503267974:
         # {"feature": "Albumin_and_Globulin_Ratio", "instances": 154, "metric_value": -0.0, "depth": 3}
         if obj[8]>1:
            # {"feature": "Total_Protiens", "instances": 122, "metric_value": 0.0, "depth": 4}
            if obj[6]>13.321873032129226:
               # {"feature": "Aspartate_Aminotransferase", "instances": 104, "metric_value": 0.0, "depth": 5}
               if obj[5]<=65.99038461538461:
                  # {"feature": "Direct_Bilirubin", "instances": 77, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=2:
                     # {"feature": "Total_Bilirubin", "instances": 47, "metric_value": 0.0, "depth": 7}
                     if obj[1]>7:
                        # {"feature": "Alamine_Aminotransferase", "instances": 27, "metric_value": -0.0, "depth": 8}
                        if obj[4]<=29.0:
                           return 'liver'
                        elif obj[4]>29.0:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=7:
                        # {"feature": "Alamine_Aminotransferase", "instances": 20, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=27:
                           return 'liver'
                        elif obj[4]>27:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]>2:
                     # {"feature": "Alamine_Aminotransferase", "instances": 30, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=43:
                        # {"feature": "Alkaline_Phosphotase", "instances": 23, "metric_value": -0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'liver'
                        elif obj[3]>291.0539499036609:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>43:
                        # {"feature": "Alkaline_Phosphotase", "instances": 7, "metric_value": -0.0, "depth": 8}
                        if obj[3]>291.0539499036609:
                           return 'liver'
                        elif obj[3]<=291.0539499036609:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[5]>65.99038461538461:
                  # {"feature": "Alkaline_Phosphotase", "instances": 27, "metric_value": -0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Total_Bilirubin", "instances": 15, "metric_value": 0.0, "depth": 7}
                     if obj[1]>4:
                        # {"feature": "Alamine_Aminotransferase", "instances": 13, "metric_value": -0.0, "depth": 8}
                        if obj[4]>61:
                           return 'liver'
                        elif obj[4]<=61:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]<=4:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[3]>291.0539499036609:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[6]<=13.321873032129226:
               # {"feature": "Direct_Bilirubin", "instances": 18, "metric_value": 0.0, "depth": 5}
               if obj[2]>2:
                  # {"feature": "Alkaline_Phosphotase", "instances": 11, "metric_value": -0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=45:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[5]>25:
                           return 'liver'
                        elif obj[5]<=25:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]>45:
                        # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[1]>11:
                           return 'liver'
                        elif obj[1]<=11:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[3]>291.0539499036609:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[2]<=2:
                  # {"feature": "Alkaline_Phosphotase", "instances": 7, "metric_value": 0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=8:
                        # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[4]>12:
                           return 'liver'
                        elif obj[4]<=12:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>8:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'normal'
            else:
               return 'liver'
         elif obj[8]<=1:
            # {"feature": "Aspartate_Aminotransferase", "instances": 32, "metric_value": 0.0, "depth": 4}
            if obj[5]>12:
               # {"feature": "Total_Protiens", "instances": 31, "metric_value": -0.0, "depth": 5}
               if obj[6]<=82:
                  # {"feature": "Direct_Bilirubin", "instances": 27, "metric_value": -0.0, "depth": 6}
                  if obj[2]<=4:
                     # {"feature": "Total_Bilirubin", "instances": 16, "metric_value": -0.0, "depth": 7}
                     if obj[1]>7:
                        # {"feature": "Alamine_Aminotransferase", "instances": 9, "metric_value": 0.0, "depth": 8}
                        if obj[4]>22:
                           return 'liver'
                        elif obj[4]<=22:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=7:
                        # {"feature": "Alkaline_Phosphotase", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]>4:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[6]>82:
                  # {"feature": "Alkaline_Phosphotase", "instances": 4, "metric_value": -0.0, "depth": 6}
                  if obj[3]<=291.0539499036609:
                     # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=7:
                        # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": -0.0, "depth": 8}
                        if obj[2]>2:
                           return 'liver'
                        elif obj[2]<=2:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]>7:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[5]<=12:
               return 'normal'
            else:
               return 'normal'
         else:
            return 'liver'
      elif obj[0]<=43.12091503267974:
         # {"feature": "Alkaline_Phosphotase", "instances": 152, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 115, "metric_value": 0.0, "depth": 4}
            if obj[8]<=68.6571116534237:
               # {"feature": "Total_Protiens", "instances": 98, "metric_value": 0.0, "depth": 5}
               if obj[6]>9.381360731502866:
                  # {"feature": "Direct_Bilirubin", "instances": 82, "metric_value": -0.0, "depth": 6}
                  if obj[2]<=2:
                     # {"feature": "Total_Bilirubin", "instances": 44, "metric_value": -0.0, "depth": 7}
                     if obj[1]>7:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 25, "metric_value": -0.0, "depth": 8}
                        if obj[5]>27:
                           return 'normal'
                        elif obj[5]<=27:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=7:
                        # {"feature": "Alamine_Aminotransferase", "instances": 19, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=97:
                           return 'normal'
                        elif obj[4]>97:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]>2:
                     # {"feature": "Total_Bilirubin", "instances": 38, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=47.28947368421053:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 29, "metric_value": 0.0, "depth": 8}
                        if obj[5]>11:
                           return 'liver'
                        elif obj[5]<=11:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>47.28947368421053:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[6]<=9.381360731502866:
                  # {"feature": "Alamine_Aminotransferase", "instances": 16, "metric_value": 0.0, "depth": 6}
                  if obj[4]>15:
                     # {"feature": "Total_Bilirubin", "instances": 14, "metric_value": -0.0, "depth": 7}
                     if obj[1]>6:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 8, "metric_value": -0.0, "depth": 8}
                        if obj[5]>20:
                           return 'liver'
                        elif obj[5]<=20:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]<=6:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=34:
                           return 'liver'
                        elif obj[5]>34:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[4]<=15:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[8]>68.6571116534237:
               # {"feature": "Total_Protiens", "instances": 17, "metric_value": 0.0, "depth": 5}
               if obj[6]<=69:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 10, "metric_value": 0.0, "depth": 6}
                  if obj[5]>31:
                     # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": -0.0, "depth": 7}
                     if obj[4]>36:
                        # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[1]>1:
                           return 'liver'
                        elif obj[1]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]<=36:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]<=31:
                     # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[4]>19:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]>8:
                           return 'liver'
                        elif obj[1]<=8:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[4]<=19:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               elif obj[6]>69:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 7, "metric_value": -0.0, "depth": 6}
                  if obj[5]>36:
                     # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[1]>8:
                        return 'liver'
                     elif obj[1]<=8:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  elif obj[5]<=36:
                     # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
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
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 37, "metric_value": 0.0, "depth": 4}
            if obj[8]<=16:
               # {"feature": "Alamine_Aminotransferase", "instances": 35, "metric_value": -0.0, "depth": 5}
               if obj[4]<=129.97142857142856:
                  # {"feature": "Total_Bilirubin", "instances": 24, "metric_value": 0.0, "depth": 6}
                  if obj[1]>6:
                     # {"feature": "Total_Protiens", "instances": 21, "metric_value": -0.0, "depth": 7}
                     if obj[6]<=75:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 14, "metric_value": -0.0, "depth": 8}
                        if obj[5]>35:
                           return 'liver'
                        elif obj[5]<=35:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[6]>75:
                        # {"feature": "Direct_Bilirubin", "instances": 7, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        elif obj[2]>2:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=6:
                     # {"feature": "Total_Protiens", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[6]>72:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=1:
                           return 'normal'
                        elif obj[2]>1:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[6]<=72:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'normal'
               elif obj[4]>129.97142857142856:
                  # {"feature": "Total_Protiens", "instances": 11, "metric_value": 0.0, "depth": 6}
                  if obj[6]<=69:
                     # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": -0.0, "depth": 7}
                     if obj[1]<=9:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": -0.0, "depth": 8}
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
                  elif obj[6]>69:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[8]>16:
               return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      else:
         return 'liver'
   elif obj[7]<=26.393063583815028:
      # {"feature": "Alkaline_Phosphotase", "instances": 213, "metric_value": 0.0, "depth": 2}
      if obj[3]<=291.0539499036609:
         # {"feature": "Age", "instances": 151, "metric_value": 0.0, "depth": 3}
         if obj[0]<=61.751437575829485:
            # {"feature": "Total_Protiens", "instances": 123, "metric_value": 0.0, "depth": 4}
            if obj[6]>20.74795261911196:
               # {"feature": "Albumin_and_Globulin_Ratio", "instances": 92, "metric_value": -0.0, "depth": 5}
               if obj[8]>1:
                  # {"feature": "Total_Bilirubin", "instances": 85, "metric_value": -0.0, "depth": 6}
                  if obj[1]<=229.86255447499877:
                     # {"feature": "Alamine_Aminotransferase", "instances": 83, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=48.53012048192771:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 59, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=43.067796610169495:
                           return 'liver'
                        elif obj[5]>43.067796610169495:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>48.53012048192771:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 24, "metric_value": 0.0, "depth": 8}
                        if obj[5]>33:
                           return 'liver'
                        elif obj[5]<=33:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[1]>229.86255447499877:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[8]<=1:
                  # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 6}
                  if obj[1]>1:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 6, "metric_value": -0.0, "depth": 7}
                     if obj[5]<=51:
                        # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=7:
                           return 'liver'
                        elif obj[2]>7:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]>51:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[1]<=1:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'normal'
            elif obj[6]<=20.74795261911196:
               # {"feature": "Direct_Bilirubin", "instances": 31, "metric_value": 0.0, "depth": 5}
               if obj[2]<=3:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 23, "metric_value": -0.0, "depth": 6}
                  if obj[5]>28:
                     # {"feature": "Alamine_Aminotransferase", "instances": 12, "metric_value": 0.0, "depth": 7}
                     if obj[4]<=50:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 7, "metric_value": -0.0, "depth": 8}
                        if obj[8]<=5:
                           return 'normal'
                        elif obj[8]>5:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>50:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[5]<=28:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 11, "metric_value": 0.0, "depth": 7}
                     if obj[8]<=1:
                        # {"feature": "Total_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[1]>6:
                           return 'liver'
                        elif obj[1]<=6:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]>1:
                        # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[1]>7:
                           return 'liver'
                        elif obj[1]<=7:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[2]>3:
                  # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 6}
                  if obj[1]>14:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[8]<=1:
                        # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=25:
                           return 'liver'
                        elif obj[4]>25:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[8]>1:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]<=14:
                     # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[4]>15:
                        return 'liver'
                     elif obj[4]<=15:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[0]>61.751437575829485:
            # {"feature": "Aspartate_Aminotransferase", "instances": 28, "metric_value": -0.0, "depth": 4}
            if obj[5]<=46.82142857142857:
               # {"feature": "Direct_Bilirubin", "instances": 19, "metric_value": 0.0, "depth": 5}
               if obj[2]>2:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 11, "metric_value": -0.0, "depth": 6}
                  if obj[8]<=7:
                     return 'liver'
                  elif obj[8]>7:
                     # {"feature": "Total_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[1]>1:
                        return 'liver'
                     elif obj[1]<=1:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[2]<=2:
                  # {"feature": "Alamine_Aminotransferase", "instances": 8, "metric_value": 0.0, "depth": 6}
                  if obj[4]<=25:
                     return 'liver'
                  elif obj[4]>25:
                     # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[1]>7:
                        return 'liver'
                     elif obj[1]<=7:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[5]>46.82142857142857:
               # {"feature": "Direct_Bilirubin", "instances": 9, "metric_value": 0.0, "depth": 5}
               if obj[2]>1:
                  return 'liver'
               elif obj[2]<=1:
                  # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=6:
                     # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[4]>24:
                        return 'normal'
                     elif obj[4]<=24:
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
      elif obj[3]>291.0539499036609:
         # {"feature": "Total_Protiens", "instances": 62, "metric_value": 0.0, "depth": 3}
         if obj[6]>47.24193548387097:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 41, "metric_value": -0.0, "depth": 4}
            if obj[8]<=37:
               # {"feature": "Direct_Bilirubin", "instances": 37, "metric_value": -0.0, "depth": 5}
               if obj[2]<=36.891891891891895:
                  # {"feature": "Age", "instances": 26, "metric_value": 0.0, "depth": 6}
                  if obj[0]>13:
                     # {"feature": "Total_Bilirubin", "instances": 25, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=35.92:
                        # {"feature": "Alamine_Aminotransferase", "instances": 16, "metric_value": 0.0, "depth": 8}
                        if obj[4]>20:
                           return 'liver'
                        elif obj[4]<=20:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]>35.92:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 9, "metric_value": 0.0, "depth": 8}
                        if obj[5]>64:
                           return 'liver'
                        elif obj[5]<=64:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[0]<=13:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[2]>36.891891891891895:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[8]>37:
               # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 5}
               if obj[2]>1:
                  # {"feature": "Age", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[0]>47:
                     # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[1]>8:
                        return 'normal'
                     elif obj[1]<=8:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[0]<=47:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[2]<=1:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[6]<=47.24193548387097:
            # {"feature": "Total_Bilirubin", "instances": 21, "metric_value": 0.0, "depth": 4}
            if obj[1]<=27:
               # {"feature": "Aspartate_Aminotransferase", "instances": 14, "metric_value": -0.0, "depth": 5}
               if obj[5]>39:
                  # {"feature": "Alamine_Aminotransferase", "instances": 9, "metric_value": -0.0, "depth": 6}
                  if obj[4]<=62:
                     # {"feature": "Age", "instances": 5, "metric_value": 0.0, "depth": 7}
                     if obj[0]>18:
                        # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[2]>4:
                           return 'liver'
                        elif obj[2]<=4:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[0]<=18:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]>62:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[5]<=39:
                  # {"feature": "Age", "instances": 5, "metric_value": 0.0, "depth": 6}
                  if obj[0]>18:
                     return 'liver'
                  elif obj[0]<=18:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            elif obj[1]>27:
               return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      else:
         return 'liver'
   else:
      return 'liver'
