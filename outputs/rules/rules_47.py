def findDecision(obj): #obj[0]: Age, obj[1]: Total_Bilirubin, obj[2]: Direct_Bilirubin, obj[3]: Alkaline_Phosphotase, obj[4]: Alamine_Aminotransferase, obj[5]: Aspartate_Aminotransferase, obj[6]: Total_Protiens, obj[7]: Albumin, obj[8]: Albumin_and_Globulin_Ratio
   # {"feature": "Age", "instances": 519, "metric_value": 0.0, "depth": 1}
   if obj[0]>44.323699421965316:
      # {"feature": "Albumin", "instances": 270, "metric_value": 0.0, "depth": 2}
      if obj[7]>26.393063583815028:
         # {"feature": "Aspartate_Aminotransferase", "instances": 152, "metric_value": 0.0, "depth": 3}
         if obj[5]<=63.19078947368421:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 112, "metric_value": 0.0, "depth": 4}
            if obj[8]>1:
               # {"feature": "Alkaline_Phosphotase", "instances": 88, "metric_value": 0.0, "depth": 5}
               if obj[3]<=291.0539499036609:
                  # {"feature": "Total_Protiens", "instances": 73, "metric_value": 0.0, "depth": 6}
                  if obj[6]<=79.89708540175712:
                     # {"feature": "Alamine_Aminotransferase", "instances": 71, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=28.056338028169016:
                        # {"feature": "Direct_Bilirubin", "instances": 44, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=4:
                           return 'liver'
                        elif obj[2]>4:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>28.056338028169016:
                        # {"feature": "Direct_Bilirubin", "instances": 27, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=8:
                           return 'liver'
                        elif obj[2]>8:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[6]>79.89708540175712:
                     # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=8:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[3]>291.0539499036609:
                  # {"feature": "Total_Bilirubin", "instances": 15, "metric_value": 0.0, "depth": 6}
                  if obj[1]>7:
                     return 'liver'
                  elif obj[1]<=7:
                     # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]>24:
                           return 'liver'
                        elif obj[4]<=24:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]<=1:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[8]<=1:
               # {"feature": "Direct_Bilirubin", "instances": 24, "metric_value": 0.0, "depth": 5}
               if obj[2]<=2:
                  # {"feature": "Total_Protiens", "instances": 14, "metric_value": -0.0, "depth": 6}
                  if obj[6]>63:
                     # {"feature": "Alkaline_Phosphotase", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[3]<=291.0539499036609:
                        # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=24:
                           return 'normal'
                        elif obj[4]>24:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[6]<=63:
                     # {"feature": "Total_Bilirubin", "instances": 7, "metric_value": 0.0, "depth": 7}
                     if obj[1]>6:
                        # {"feature": "Alamine_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[4]>14:
                           return 'liver'
                        elif obj[4]<=14:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]<=6:
                        return 'liver'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[2]>2:
                  return 'liver'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[5]>63.19078947368421:
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 40, "metric_value": 0.0, "depth": 4}
            if obj[8]<=9:
               return 'liver'
            elif obj[8]>9:
               # {"feature": "Total_Bilirubin", "instances": 17, "metric_value": 0.0, "depth": 5}
               if obj[1]>11:
                  # {"feature": "Total_Protiens", "instances": 11, "metric_value": -0.0, "depth": 6}
                  if obj[6]<=66:
                     # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=61:
                        # {"feature": "Alkaline_Phosphotase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[3]<=291.0539499036609:
                           return 'normal'
                        elif obj[3]>291.0539499036609:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>61:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[6]>66:
                     # {"feature": "Alkaline_Phosphotase", "instances": 5, "metric_value": -0.0, "depth": 7}
                     if obj[3]>291.0539499036609:
                        return 'liver'
                     elif obj[3]<=291.0539499036609:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=6:
                           return 'normal'
                        elif obj[2]>6:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[1]<=11:
                  # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 6}
                  if obj[4]>42:
                     return 'liver'
                  elif obj[4]<=42:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            else:
               return 'liver'
         else:
            return 'liver'
      elif obj[7]<=26.393063583815028:
         # {"feature": "Alkaline_Phosphotase", "instances": 118, "metric_value": 0.0, "depth": 3}
         if obj[3]<=291.0539499036609:
            # {"feature": "Direct_Bilirubin", "instances": 81, "metric_value": 0.0, "depth": 4}
            if obj[2]>1:
               # {"feature": "Alamine_Aminotransferase", "instances": 69, "metric_value": 0.0, "depth": 5}
               if obj[4]>10:
                  # {"feature": "Total_Protiens", "instances": 68, "metric_value": -0.0, "depth": 6}
                  if obj[6]>49.705882352941174:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 46, "metric_value": 0.0, "depth": 7}
                     if obj[5]>13:
                        # {"feature": "Total_Bilirubin", "instances": 45, "metric_value": 0.0, "depth": 8}
                        if obj[1]>1:
                           return 'liver'
                        elif obj[1]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]<=13:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[6]<=49.705882352941174:
                     # {"feature": "Total_Bilirubin", "instances": 22, "metric_value": -0.0, "depth": 7}
                     if obj[1]>7:
                        # {"feature": "Albumin_and_Globulin_Ratio", "instances": 15, "metric_value": -0.0, "depth": 8}
                        if obj[8]<=8:
                           return 'liver'
                        elif obj[8]>8:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=7:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=30:
                           return 'normal'
                        elif obj[5]>30:
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
            elif obj[2]<=1:
               # {"feature": "Total_Protiens", "instances": 12, "metric_value": 0.0, "depth": 5}
               if obj[6]>7:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 7, "metric_value": -0.0, "depth": 6}
                  if obj[8]>5:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": -0.0, "depth": 7}
                     if obj[5]>33:
                        # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[1]<=4:
                           return 'liver'
                        elif obj[1]>4:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[5]<=33:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]<=5:
                     # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": -0.0, "depth": 7}
                     if obj[1]>6:
                        return 'liver'
                     elif obj[1]<=6:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[6]<=7:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": 0.0, "depth": 6}
                  if obj[5]>23:
                     return 'liver'
                  elif obj[5]<=23:
                     return 'normal'
                  else:
                     return 'normal'
               else:
                  return 'liver'
            else:
               return 'liver'
         elif obj[3]>291.0539499036609:
            # {"feature": "Total_Protiens", "instances": 37, "metric_value": 0.0, "depth": 4}
            if obj[6]<=70.74159609440183:
               # {"feature": "Total_Bilirubin", "instances": 32, "metric_value": 0.0, "depth": 5}
               if obj[1]<=54.96875:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 20, "metric_value": -0.0, "depth": 6}
                  if obj[8]>5:
                     # {"feature": "Alamine_Aminotransferase", "instances": 15, "metric_value": -0.0, "depth": 7}
                     if obj[4]>16:
                        # {"feature": "Direct_Bilirubin", "instances": 14, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=22:
                           return 'liver'
                        elif obj[2]>22:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=16:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[8]<=5:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[1]>54.96875:
                  # {"feature": "Direct_Bilirubin", "instances": 12, "metric_value": 0.0, "depth": 6}
                  if obj[2]>27:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 9, "metric_value": -0.0, "depth": 7}
                     if obj[8]<=6:
                        # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": -0.0, "depth": 8}
                        if obj[4]>46:
                           return 'liver'
                        elif obj[4]<=46:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[8]>6:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]<=27:
                     # {"feature": "Albumin_and_Globulin_Ratio", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[8]<=5:
                        return 'liver'
                     elif obj[8]>5:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[6]>70.74159609440183:
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
         # {"feature": "Albumin_and_Globulin_Ratio", "instances": 154, "metric_value": 0.0, "depth": 3}
         if obj[8]>1:
            # {"feature": "Alkaline_Phosphotase", "instances": 123, "metric_value": 0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Aspartate_Aminotransferase", "instances": 94, "metric_value": 0.0, "depth": 5}
               if obj[5]>11:
                  # {"feature": "Total_Bilirubin", "instances": 93, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=133.61172472472458:
                     # {"feature": "Total_Protiens", "instances": 89, "metric_value": -0.0, "depth": 7}
                     if obj[6]>10.962512487800808:
                        # {"feature": "Direct_Bilirubin", "instances": 75, "metric_value": -0.0, "depth": 8}
                        if obj[2]<=22:
                           return 'liver'
                        elif obj[2]>22:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[6]<=10.962512487800808:
                        # {"feature": "Direct_Bilirubin", "instances": 14, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=3:
                           return 'liver'
                        elif obj[2]>3:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>133.61172472472458:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[5]<=11:
                  return 'liver'
               else:
                  return 'liver'
            elif obj[3]>291.0539499036609:
               # {"feature": "Total_Protiens", "instances": 29, "metric_value": 0.0, "depth": 5}
               if obj[6]>67:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 21, "metric_value": -0.0, "depth": 6}
                  if obj[5]>51:
                     return 'liver'
                  elif obj[5]<=51:
                     # {"feature": "Direct_Bilirubin", "instances": 10, "metric_value": 0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[4]>25:
                           return 'liver'
                        elif obj[4]<=25:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[2]<=1:
                        # {"feature": "Alamine_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[4]>25:
                           return 'normal'
                        elif obj[4]<=25:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[6]<=67:
                  # {"feature": "Total_Bilirubin", "instances": 8, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=8:
                     # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=2:
                        # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[4]>25:
                           return 'normal'
                        elif obj[4]<=25:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'liver'
                  elif obj[1]>8:
                     # {"feature": "Direct_Bilirubin", "instances": 4, "metric_value": 0.0, "depth": 7}
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
            else:
               return 'liver'
         elif obj[8]<=1:
            # {"feature": "Alkaline_Phosphotase", "instances": 31, "metric_value": 0.0, "depth": 4}
            if obj[3]<=291.0539499036609:
               # {"feature": "Total_Protiens", "instances": 22, "metric_value": 0.0, "depth": 5}
               if obj[6]>7:
                  # {"feature": "Total_Bilirubin", "instances": 19, "metric_value": -0.0, "depth": 6}
                  if obj[1]>7:
                     # {"feature": "Direct_Bilirubin", "instances": 12, "metric_value": -0.0, "depth": 7}
                     if obj[2]<=2:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 8, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=50:
                           return 'liver'
                        elif obj[5]>50:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]>2:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[5]>19:
                           return 'liver'
                        elif obj[5]<=19:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[1]<=7:
                     # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": -0.0, "depth": 7}
                     if obj[4]<=47:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 5, "metric_value": -0.0, "depth": 8}
                        if obj[5]<=26:
                           return 'liver'
                        elif obj[5]>26:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]>47:
                        # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=2:
                           return 'liver'
                        elif obj[2]>2:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  else:
                     return 'liver'
               elif obj[6]<=7:
                  # {"feature": "Direct_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=2:
                     # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[1]>6:
                        return 'liver'
                     elif obj[1]<=6:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[3]>291.0539499036609:
               # {"feature": "Alamine_Aminotransferase", "instances": 9, "metric_value": 0.0, "depth": 5}
               if obj[4]>28:
                  # {"feature": "Direct_Bilirubin", "instances": 6, "metric_value": -0.0, "depth": 6}
                  if obj[2]>1:
                     return 'liver'
                  elif obj[2]<=1:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[4]<=28:
                  # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[1]>6:
                     # {"feature": "Direct_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[2]<=3:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=16:
                           return 'normal'
                        elif obj[5]>16:
                           return 'liver'
                        else:
                           return 'liver'
                     else:
                        return 'normal'
                  elif obj[1]<=6:
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
            # {"feature": "Albumin_and_Globulin_Ratio", "instances": 70, "metric_value": 0.0, "depth": 4}
            if obj[8]<=76:
               # {"feature": "Total_Protiens", "instances": 67, "metric_value": -0.0, "depth": 5}
               if obj[6]>43.865671641791046:
                  # {"feature": "Alamine_Aminotransferase", "instances": 44, "metric_value": -0.0, "depth": 6}
                  if obj[4]<=51.25:
                     # {"feature": "Total_Bilirubin", "instances": 28, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=16:
                        # {"feature": "Direct_Bilirubin", "instances": 22, "metric_value": -0.0, "depth": 8}
                        if obj[2]>1:
                           return 'liver'
                        elif obj[2]<=1:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[1]>16:
                        # {"feature": "Direct_Bilirubin", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[2]>23:
                           return 'liver'
                        elif obj[2]<=23:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'liver'
                  elif obj[4]>51.25:
                     # {"feature": "Direct_Bilirubin", "instances": 16, "metric_value": 0.0, "depth": 7}
                     if obj[2]>1:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 12, "metric_value": 0.0, "depth": 8}
                        if obj[5]>56:
                           return 'liver'
                        elif obj[5]<=56:
                           return 'normal'
                        else:
                           return 'normal'
                     elif obj[2]<=1:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 8}
                        if obj[5]>41:
                           return 'liver'
                        elif obj[5]<=41:
                           return 'normal'
                        else:
                           return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[6]<=43.865671641791046:
                  # {"feature": "Direct_Bilirubin", "instances": 23, "metric_value": 0.0, "depth": 6}
                  if obj[2]<=3:
                     # {"feature": "Aspartate_Aminotransferase", "instances": 17, "metric_value": 0.0, "depth": 7}
                     if obj[5]>16:
                        # {"feature": "Alamine_Aminotransferase", "instances": 14, "metric_value": -0.0, "depth": 8}
                        if obj[4]>27:
                           return 'liver'
                        elif obj[4]<=27:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[5]<=16:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[2]>3:
                     # {"feature": "Alamine_Aminotransferase", "instances": 6, "metric_value": 0.0, "depth": 7}
                     if obj[4]>15:
                        # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[1]>13:
                           return 'liver'
                        elif obj[1]<=13:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[4]<=15:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[8]>76:
               # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 5}
               if obj[5]>29:
                  # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 6}
                  if obj[1]<=2:
                     return 'liver'
                  elif obj[1]>2:
                     return 'normal'
                  else:
                     return 'normal'
               elif obj[5]<=29:
                  return 'normal'
               else:
                  return 'normal'
            else:
               return 'normal'
         elif obj[3]>291.0539499036609:
            # {"feature": "Total_Protiens", "instances": 25, "metric_value": 0.0, "depth": 4}
            if obj[6]>53:
               # {"feature": "Direct_Bilirubin", "instances": 15, "metric_value": -0.0, "depth": 5}
               if obj[2]>13:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 8, "metric_value": -0.0, "depth": 6}
                  if obj[8]<=6:
                     # {"feature": "Alamine_Aminotransferase", "instances": 4, "metric_value": 0.0, "depth": 7}
                     if obj[4]>25:
                        return 'liver'
                     elif obj[4]<=25:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[8]>6:
                     return 'liver'
                  else:
                     return 'liver'
               elif obj[2]<=13:
                  # {"feature": "Alamine_Aminotransferase", "instances": 7, "metric_value": -0.0, "depth": 6}
                  if obj[4]>37:
                     # {"feature": "Total_Bilirubin", "instances": 5, "metric_value": -0.0, "depth": 7}
                     if obj[1]>21:
                        # {"feature": "Aspartate_Aminotransferase", "instances": 3, "metric_value": 0.0, "depth": 8}
                        if obj[5]<=57:
                           return 'normal'
                        elif obj[5]>57:
                           return 'liver'
                        else:
                           return 'liver'
                     elif obj[1]<=21:
                        return 'liver'
                     else:
                        return 'liver'
                  elif obj[4]<=37:
                     return 'liver'
                  else:
                     return 'liver'
               else:
                  return 'liver'
            elif obj[6]<=53:
               # {"feature": "Direct_Bilirubin", "instances": 10, "metric_value": 0.0, "depth": 5}
               if obj[2]>3:
                  # {"feature": "Albumin_and_Globulin_Ratio", "instances": 6, "metric_value": 0.0, "depth": 6}
                  if obj[8]>1:
                     # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[1]>13:
                        return 'liver'
                     elif obj[1]<=13:
                        return 'normal'
                     else:
                        return 'normal'
                  elif obj[8]<=1:
                     # {"feature": "Total_Bilirubin", "instances": 3, "metric_value": 0.0, "depth": 7}
                     if obj[1]>15:
                        return 'liver'
                     elif obj[1]<=15:
                        return 'normal'
                     else:
                        return 'normal'
                  else:
                     return 'liver'
               elif obj[2]<=3:
                  # {"feature": "Aspartate_Aminotransferase", "instances": 4, "metric_value": -0.0, "depth": 6}
                  if obj[5]<=25:
                     return 'liver'
                  elif obj[5]>25:
                     # {"feature": "Total_Bilirubin", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[1]<=9:
                        # {"feature": "Alamine_Aminotransferase", "instances": 2, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=30:
                           return 'liver'
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
         else:
            return 'liver'
      else:
         return 'liver'
   else:
      return 'liver'
