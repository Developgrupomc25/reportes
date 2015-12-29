<html>
    <head>
        <style type="text/css">
            ${css}
            h1{
                  font-family:"Times New Roman", Georgia, Serif;color: #086A87;
                    text-align:left;
                    font-size:30px;
                    font-weight:bold;"
              }

               h2{
                color:#086A87;
                font-size:23px;
                font-family:'Brodway';
              }
              h3{
                color:#086A87;
                font-size:20px;
                font-family:'Brodway';
              }
              hr{
                background-color:black;
                line-height:3px;
                width:90%;

              }
              hr.lol{
                background-color:black;
                line-height:3px;
                margin-right:10%;
                margin-left: 5%;
                

              }
               

        </style>
    </head>
    <body>
       %for o in objects :
            <% setLang(user.lang) %>  
            <div class="contenedor_principal">
                <div class="contenedor_contenido">
                  <div class="act_as_table">
                        <div class="act_as_row">
                            <div class="act_as_cell" style="width:20%;">
                                <div style="position: relative;">
                                    <div style="position: absolute; top: 10px; bottom: 0px;">
                                        ${helper.embed_image('jpeg',str(o.company_id.logo),130)}                         
                                    </div>                               
                                </div>
                            </div>
                            <div class="act_as_cell" text-align="right" >
                                  <h1> Orden de Recepcion  ${o.name}</h1>
                                    
                            </div>
                           
                           
                    </div> <!--AQUI CIERRA PRIMERA FILA DE ENCABEZADO-->
                </div> <!--AQUI ACABA LA PRIMER TABLA-->

                <hr>

<br>
<br>
<br>


                <div class="act_as_table">
                  <div class="act_as_row">
                      <div class="act_as_cell" style="font-size:15px;">
                          <b >Fecha de Recepcion:</b>${o.fecha_alta}<br>
                          <b >Estatus:</b> ${o.deliver_bool}<br>
                      </div>
                      <div class="act_as_cell" style="font-size:15px;">
                          <b >A Facturar:</b> ${o.invoiced or 'NO'}<br>
                          <b>Servicio:</b>${o.product_id.name}<br>
                      </div>
                  </div>
              
                  
                  <div class="act_as_row">
                      <div class="act_as_cell" style="font-size:15px;">
                          <h2> Datos de la Empresa</h2>
                             <b>Centro de Servicio: </b> ${o.partner_id.name}
                              <br>
                              %if o.partner_id.city != False:
                              <b>Ciudad:</b> ${o.partner_id.city}
                              <br>
                              %endif
                              %if o.partner_id.state_id.name != None:
                              <b>Estado:</b> ${o.partner_id.state_id.name}
                              <br>
                              %endif
                              %if o.partner_id.street != 0:
                              <b>Calle 1:</b> ${o.partner_id.street}
                              <br>
                              %endif
                              %if o.partner_id.street2 != 0:
                              <b>Calle 2:</b> ${o.partner_id.street2}
                              <br>
                              %endif
                              %if o.partner_id.phone != 0:
                              <b>Telefono:</b> ${o.partner_id.phone}
                              <br>
                              %endif
                              %if o.partner_id.website != 0:
                              <b>Sitio Web:</b> ${o.partner_id.website}
                              %endif
                      </div>
                      <div class="act_as_cell" style="font-size:15px;">
                              <h2> Datos del Cliente </h2>
                                                                              
                               <b>Nombre:</b> ${o.empresaNombre.name}
                               <br>
                               <b>Correo Electronico:</b> ${o.empresaNombre.work_email}
                               <br>
                               <b>Telefono de la Empresa:</b> ${o.empresaNombre.work_phone}
                               <br>
                               <b>Telefono Personal:</b> ${o.empresaNombre.mobile_phone}
                            
                      </div>
                  </div>
                 
                </div>
<br>
<br>
                    <div class="as_act_row">
                       <div class="act_as_cell" style="width:20%; font-size:15px;">
                                <h2>Del Vehiculo:</h2>
                                <b>Nombre del vehiculo:</b> ${o.modelo_id.model_id.name or ''}
                                <br>
                                <b>Placas:</b> ${o.modelo_id.license_plate or ''}
                                <br>
                                <b>Nombre del Conductor:</b> ${o.modelo_id.driver_id.name or ''}
                                <br>
                                <b>Odometro:</b> ${o.modelo_id.odometer or ''}
                                <br>
                                %if o.modelo_id.noseriemc != False:
                                <br>
                                <b>Numero de Serie:</b> ${o.modelo_id.noseriemc or ''}
                                <br>
                                %endif
                                %if o.modelo_id.noeconomicomc != False:
                                <b>Numero Economico:</b> ${o.modelo_id.noeconomicomc or ''}
                                <br>
                                %endif
                                %if o.modelo_id.colormc !=0:
                                <b>Color:</b> ${o.modelo_id.colormc}
                                <br>
                                %endif
                                %if o.modelo_id.modelomc != 0:
                                <b> Modelo:</b>${o.modelo_id.modelomc}
                                <br>
                                %endif
                        
                      </div>
                    
                      <div class="act_as_cell"  style="width:15%; font-size:15px;">
                            <h2>Equipo Hidrahulico</h2>
                               %if o.modelo_id.modelomc != 0:
                               <b>Modelo:</b> ${o.modelo_id.modelomc}<br>
                               %endif
                               %if o.modelo_id.anomc != 0:
                               <b>Año:</b> ${o.modelo_id.anomc}<br>
                               %endif
                               %if o.modelo_id.odometromc !=0:
                               <b>Odometro:</b> ${o.modelo_id.odometromc}<br>
                               %endif
                               %if o.modelo_id.colormc !=0:
                               <b>Color:</b> ${o.modelo_id.colormc}<br>
                               %endif
                               %if o.modelo_id.marcamc !=0:
                               <b>Marca:</b> ${o.modelo_id.marcamc}<br>
                               %endif
                               %if o.modelo_id.capacidadmc !=0:
                               <b>Capacidad:</b> ${o.modelo_id.capacidadmc}<br>
                               %endif
                        
                      </div>
                      
                  </div>

               <br>
               <br>
               <br>
               <br>
               <br>
               <br>
               <br>
               <br>
               <br>
               <br>
               <br>
               <br>




            </div>  <!--contenedor contenido-->
             <table>
                  <tr>
                   <td>
                    <%! from time import strftime as time %>
                        <b> <i>Fecha de Impresion </b> </i>${"%d de %B" | time}
                    </td>
                    <td align="right">
                       <p align="right"> Hora de impresion ${"%P hrs" | time} </p>
                    </td>
                  </tr>
                </table>
          </div> <!--contenedor principal-->
           
        %endfor
        
      </body>
</html>
 

 
 

     
