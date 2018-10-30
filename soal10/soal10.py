import shapefile 
w=shapefile.Writer() 
w.shapeType  
w.field("kolom1","C") 
w.field("kolom2","C")  
w.record("ngek","satu") 
w.record("crot","dua")    
w.poly(parts=[[[1,3],[5,3], [3,7], [1,3]]],shapeType=shapefile.POLYLINE)
w.poly(parts=[[[5,7],[9,7], [7,11], [5,7]]],shapeType=shapefile.POLYLINE)    
w.save("soal10")