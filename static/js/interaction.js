/**
 * Function to navigate NEXT/BACK scenarios
 * @param {*} next next=1 or 0
 */
function navigate(next) {
    if ( !$('#user').val() ) {
        alert("Please enter Your Name to continue.");
        return
    }
<<<<<<< HEAD

=======
>>>>>>> e58740ea3b9bf6c9746ef6279ada3124ac6c407c
    if ( !$('#exercise').val() ) { 
        alert("You must choose an exercise to continue.");
        return
    }
<<<<<<< HEAD

    save_resolution();

    if (next) {
        if (index<n-1) {
            index += 1;
            remove_all();
            scenario = new Scenario(data[index]);       
        } else {
            alert("Data saved! Also end of exercise reached. Thank you!");
=======
    save_resolution();
    if (next) {
        if (index<n-1) {
            index += 1;            
        } else {
            alert("Data saved! Also end of exercise reached. Thank you!");
            return
>>>>>>> e58740ea3b9bf6c9746ef6279ada3124ac6c407c
        }        
    } else {
        if (index>0) {
            index -= 1;
<<<<<<< HEAD
            remove_all();
            scenario = new Scenario(data[index]);
        } else {
            alert("Data saved! And you're at the first scenario of this exercise."); 
        } 
    }
=======
        } else {
            alert("Data saved! And you're at the first scenario of this exercise."); 
            return
        } 
    }
    remove_all();
    scenario = new Scenario(data[index]);
>>>>>>> e58740ea3b9bf6c9746ef6279ada3124ac6c407c
    $('#current-index').html(`${index+1}/${n}`);
}


/**
 * Function to remove all elements
 */
function remove_all() {    
    airway_layer.removeChildren();     
    waypoint_layer.removeChildren();  
    conflict_layer.removeChildren();  
    maneuver_layer.removeChildren();  
    aircraft_layer.removeChildren();  
    text_layer.removeChildren();
    scenario = null;      
}


<<<<<<< HEAD

/**
 * Function to show data 
 */
function show_data(data) {
    $('#data').html(JSON.stringify(data));
=======
/**
 * Function to init global resolutions var upon loading data
 * @param {*} data 
 * @param {*} n 
 */
function init_global_resolutions(data, n) {    
    resolutions = Array(n);
    for (let i=0; i<n; i++) {
        resolution = {};
        let names = Object.keys(data[i].aircrafts);
        for (let j=0; j<names.length; j++) {
            let name = names[j];
            resolution[name] = { "turn_angle" : null, "dct" : null, "last_position": null };
        }
        resolutions[i] = resolution;
    }
>>>>>>> e58740ea3b9bf6c9746ef6279ada3124ac6c407c
}


/**
 * Function to request exercise data from the server
 * @param {*} name 
 */
function request_exercise(name) {
    $('#next-btn').prop('disabled', true);
    $('#back-btn').prop('disabled', true);
    remove_all();
    data = null;
    n = null;
    index = -1;    
    $.get( "/handlers/load.php", {exercise: $('#exercise').val()} )
        .done(function( response ) {
            response = JSON.parse(response);
            if ( response.status ) {
                $('#status').html(`${$('#exercise').val()} loaded.`);
                data = JSON.parse(response.data);
                n = data.length;
<<<<<<< HEAD
=======
                init_global_resolutions(data, n);
>>>>>>> e58740ea3b9bf6c9746ef6279ada3124ac6c407c
                $('#current-index').html(`/${n}`);
                $('#next-btn').prop('disabled', false);
                $('#back-btn').prop('disabled', false);
            }                
            else
                alert(response) 
        })
}



/**
 * Function to send resolution to server and save
 */
function save_resolution() {
    if (index<0 | index>n-1)
        return
    let names = Object.keys(scenario.aircrafts);
    for (let i=0; i<names.length; i++) {
        let name = names[i];
<<<<<<< HEAD
        data[index].aircrafts[name]['resolution'] = scenario.aircrafts[name].resolution;
=======
        // save resolution into original data var
        data[index].aircrafts[name]['resolution'] = scenario.aircrafts[name].resolution;
        // save resolution to global resolutions var
        resolutions[index][name] = scenario.aircrafts[name].resolution;
>>>>>>> e58740ea3b9bf6c9746ef6279ada3124ac6c407c
    }
    let save_data = {
        "action" : "save",
        "scenario_index" : index,
        "exercise" : $('#exercise').val(),
        "name" : $('#user').val(),
        "scenario_data" : JSON.stringify(data[index]),
<<<<<<< HEAD
        "resolution_data" : JSON.stringify(data[index].aircrafts)
=======
        // "resolution_data" : JSON.stringify(data[index].aircrafts),
        "resolution_data" : JSON.stringify(resolutions[index]),
>>>>>>> e58740ea3b9bf6c9746ef6279ada3124ac6c407c
    };
    $.post('/handlers/save.php', save_data)
        .done(function(response) {
            response = JSON.parse(response);
            if (response.status) {
                save_count += 1;
<<<<<<< HEAD
                $('#status').html(`Number of records saved: ${save_count}.`);
=======
                $('#status').html(`Records saved: ${save_count}.`);
>>>>>>> e58740ea3b9bf6c9746ef6279ada3124ac6c407c
            } else {
                alert("Data couldn't be saved properly. Please contact us!");
            }
        })
}


<<<<<<< HEAD

/**
 * 
 * @param {*} n 
 */
function generate_data(n) {
    
    let wp_names = ['wp1', 'wp2', 'wp3', 'wp4', 'wp5', 'wp6', 'wp7', 'wp8', 'wp9', 'wp10'];
    let aw_names = ['aw1', 'aw2', 'aw3', 'aw4', 'aw5', 'aw6', 'aw7', 'aw8', 'aw9', 'aw10'];
    let ac_names = ['ac1', 'ac2', 'ac3', 'ac4', 'ac5', 'ac6', 'ac7', 'ac8', 'ac9', 'ac10'];        
    
    let scenarios = [];    
    
    for (k=0; k<n; k++) {
        // Scenarios loop (10 scenarios)
        let scenario = { waypoints : {}, airways : {}, aircrafts : {} };
    
        for (i=0; i<wp_names.length; i++ ) {
            let name = wp_names[i];    
            scenario.waypoints[name] = {
                x : Math.random() * PY2JS_SCALE,
                y : Math.random() * PY2JS_SCALE,
            }    
        }
        
        for (i=0; i<aw_names.length; i++) {
            let name = aw_names[i];        
            let m = Math.floor(Math.random() * Math.floor(wp_names.length));
            let n = Math.floor(Math.random() * Math.floor(wp_names.length));            
            scenario.airways[name] = {
                start : wp_names[m],
                end: wp_names[n]
            }
        }
        
        for (i=0; i<ac_names.length; i++) {
            let name = ac_names[i];
            let x = Math.random() * PY2JS_SCALE;
            let y = Math.random() * PY2JS_SCALE;
            let sign_x = Math.random() < 0.5 ? -1 : 1;
            let sign_y = Math.random() < 0.5 ? -1 : 1;
            let dir_x = sign_x * Math.random() * PY2JS_SCALE;
            let dir_y = sign_y * Math.random() * PY2JS_SCALE;
            dir_x = dir_x / (Math.sqrt(dir_x**2 + dir_y**2));
            dir_y = dir_y / (Math.sqrt(dir_x**2 + dir_y**2));
            scenario.aircrafts[name] = {
                x : x,
                y : y,
                dir_x : dir_x,
                dir_y : dir_y
            }
        }       
        scenarios.push(scenario);
    }
    return scenarios
}



=======
>>>>>>> e58740ea3b9bf6c9746ef6279ada3124ac6c407c
$('#waypoint-cb').on('change', function(){
    waypoint_layer.visible = $('#waypoint-cb').prop('checked');
})
$('#airway-cb').on('change', function(){
    airway_layer.visible = $('#airway-cb').prop('checked');
})
