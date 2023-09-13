import base64
from png_upload import upload_image_to_imgbb
import json
from PIL import Image, ImageDraw, ImageFont
import math
from io import BytesIO


# star chart
# armor, struct, corridor
# mouvement, thrusters, engine room
# shield, small and large
# weapons including point defense
# crew
# storage
# utilities, the rest like doors




parts_resources = [
    {"ID": "cosmoteer.airlock", "Resources": [["steel", "8"], ["coil", "4"]]},
    {"ID": "cosmoteer.armor", "Resources": [["steel", "8"]]},
    {"ID": "cosmoteer.armor_1x2_wedge", "Resources": [["steel", "8"]]},
    {"ID": "cosmoteer.armor_1x3_wedge", "Resources": [["steel", "12"]]},
    {"ID": "cosmoteer.armor_2x1", "Resources": [["steel", "16"]]},
    {"ID": "cosmoteer.armor_structure_hybrid_1x1", "Resources": [["steel", "5"]]},
    {"ID": "cosmoteer.armor_structure_hybrid_1x2", "Resources": [["steel", "10"]]},
    {"ID": "cosmoteer.armor_structure_hybrid_1x3", "Resources": [["steel", "15"]]},
    {"ID": "cosmoteer.armor_structure_hybrid_tri", "Resources": [["steel", "3"]]},
    {"ID": "cosmoteer.armor_tri", "Resources": [["steel", "2"]]},
    {"ID": "cosmoteer.armor_wedge", "Resources": [["steel", "4"]]},
    {"ID": "cosmoteer.cannon_deck","Resources": [["steel", "200"], ["coil2", "30"], ["tristeel", "30"], ["bullet", "100"]]},
    {"ID": "cosmoteer.cannon_large", "Resources": [["steel", "84"], ["coil", "29"], ["bullet", "64"]]},
    {"ID": "cosmoteer.cannon_med", "Resources": [["steel", "48"], ["coil", "8"], ["bullet", "16"]]},
    {"ID": "cosmoteer.control_room_large","Resources": [["steel", "160"], ["coil2", "70"], ["processor", "10"]]},
    {"ID": "cosmoteer.control_room_med","Resources": [["steel", "80"], ["coil2", "35"], ["processor", "5"]]},
    {"ID": "cosmoteer.control_room_small","Resources": [["steel", "32"], ["coil2", "14"], ["processor", "2"]]},
    {"ID": "cosmoteer.conveyor", "Resources": [["steel", "4"], ["coil", "1"]]},
    {"ID": "cosmoteer.corridor", "Resources": [["steel", "4"]]},
    {"ID": "cosmoteer.crew_quarters_med", "Resources": [["steel", "48"]]},
    {"ID": "cosmoteer.crew_quarters_small", "Resources": [["steel", "24"]]},
    {"ID": "cosmoteer.disruptor", "Resources": [["steel", "40"], ["coil", "20"]]},
    {"ID": "cosmoteer.door", "Resources": [["coil", "1"]]},
    {"ID": "cosmoteer.engine_room","Resources": [["steel", "72"], ["coil2", "28"], ["tristeel", "9"]]},
    {"ID": "cosmoteer.explosive_charge","Resources": [["steel", "16"], ["coil", "4"], ["sulfur", "10"]]},
    {"ID": "cosmoteer.factory_ammo","Resources": [["steel", "32"], ["coil", "24"], ["tristeel", "4"], ["sulfur", "5"]]},
    {"ID": "cosmoteer.factory_coil","Resources": [["steel", "80"], ["coil", "80"], ["processor", "8"], ["copper", "10"]]},
    {"ID": "cosmoteer.factory_coil2","Resources": [["steel", "104"], ["coil2", "58"], ["processor", "12"], ["copper", "10"], ["coil", "40"] ]},
    {"ID": "cosmoteer.factory_diamond","Resources": [["steel", "48"], ["coil2", "118"], ["tristeel", "67"], ["carbon", "20"]]},
    {"ID": "cosmoteer.factory_emp","Resources": [["steel", "96"], ["coil2", "32"], ["diamond", "2"], ["iron", "5"], ["copper", "5"]]},
    {"ID": "cosmoteer.factory_he","Resources": [["steel", "76"], ["coil2", "27"], ["processor", "2"], ["iron", "5"], ["sulfur", "5"]]},
    {"ID": "cosmoteer.factory_mine","Resources": [["steel", "96"], ["coil2", "50"], ["tristeel", "13"], ["iron", "5"], ["bullet", "20"]]},
    {"ID": "cosmoteer.factory_nuke","Resources": [["steel", "136"], ["coil2", "62"], ["enriched_uranium", "4"], ["iron", "5"], ["uranium", "5"]]},
    {"ID": "cosmoteer.factory_processor","Resources": [["steel", "80"], ["coil2", "100"], ["diamond", "12"], ["coil", "40"], ["gold", "10"]]},
    {"ID": "cosmoteer.factory_steel","Resources": [["steel", "120"], ["coil", "90"], ["coil2", "60"], ["iron", "20"]]},
    {"ID": "cosmoteer.factory_tristeel","Resources": [["steel", "120"], ["coil2", "100"], ["diamond", "8"], ["tritanium", "20"]]},
    {"ID": "cosmoteer.factory_uranium","Resources": [["steel", "80"], ["coil2", "80"], ["enriched_uranium", "32"], ["uranium", "20"]]},
    {"ID": "cosmoteer.fire_extinguisher", "Resources": [["steel", "8"], ["coil", "1"]]},
    {"ID": "cosmoteer.flak_cannon_large","Resources": [["steel", "200"], ["coil2", "30"], ["bullet", "92"]]},
    {"ID": "cosmoteer.hyperdrive_beacon","Resources": [["steel", "160"], ["coil2", "40"], ["diamond", "6"]]},
    {"ID": "cosmoteer.hyperdrive_small","Resources": [["steel", "40"], ["coil2", "30"]]},
    {"ID": "cosmoteer.ion_beam_emitter","Resources": [["steel", "60"], ["coil2", "15"], ["diamond", "1"]]},
    {"ID": "cosmoteer.ion_beam_prism","Resources": [["steel", "16"], ["coil2", "2"], ["diamond", "1"]]},
    {"ID": "cosmoteer.laser_blaster_large","Resources": [["steel", "96"], ["coil", "36"]]},
    {"ID": "cosmoteer.laser_blaster_small","Resources": [["steel", "32"], ["coil", "12"]]},
    {"ID": "cosmoteer.mining_laser_small","Resources": [["steel", "96"], ["coil", "36"]]},
    {"ID": "cosmoteer.missile_launcher","Resources": [["steel", "60"], ["coil2", "20"], ["processor", "1"]]},
    {"ID": "cosmoteer.point_defense", "Resources": [["steel", "8"], ["coil", "8"]]},
    {"ID": "cosmoteer.power_storage", "Resources": [["steel", "32"], ["coil", "32"]]},
    {"ID": "cosmoteer.railgun_accelerator","Resources": [["steel", "76"], ["coil2", "12"], ["tristeel", "10"]]},
    {"ID": "cosmoteer.railgun_launcher","Resources": [["steel", "100"], ["coil2", "10"], ["tristeel", "10"]]},
    {"ID": "cosmoteer.railgun_loader","Resources": [["steel", "60"], ["coil2", "30"], ["tristeel", "10"], ["bullet", "46"]]},
    {"ID": "cosmoteer.reactor_large","Resources": [["steel", "120"], ["coil2", "80"], ["enriched_uranium", "24"]]},
    {"ID": "cosmoteer.reactor_med","Resources": [["steel", "72"], ["coil2", "54"], ["enriched_uranium", "16"]]},
    {"ID": "cosmoteer.reactor_small","Resources": [["steel", "32"], ["coil", "82"], ["enriched_uranium", "8"]]},
    {"ID": "cosmoteer.roof_headlight", "Resources": [["steel", "4"], ["coil", "2"]]},
    {"ID": "cosmoteer.roof_light", "Resources": [["steel", "4"], ["coil", "1"]]},
    {"ID": "cosmoteer.sensor_array","Resources": [["steel", "76"], ["coil2", "27"], ["processor", "4"]]},
    {"ID": "cosmoteer.shield_gen_large","Resources": [["steel", "120"], ["coil2", "30"], ["diamond", "2"]]},
    {"ID": "cosmoteer.shield_gen_small","Resources": [["steel", "40"], ["coil", "40"]]},
    {"ID": "cosmoteer.storage_2x2", "Resources": [["steel", "48"]]},
    {"ID": "cosmoteer.storage_3x2", "Resources": [["steel", "72"]]},
    {"ID": "cosmoteer.storage_3x3", "Resources": [["steel", "108"]]},
    {"ID": "cosmoteer.storage_4x3", "Resources": [["steel", "144"]]},
    {"ID": "cosmoteer.storage_4x4", "Resources": [["steel", "192"]]},
    {"ID": "cosmoteer.structure", "Resources": [["steel", "2"]]},
    {"ID": "cosmoteer.structure_1x2_wedge", "Resources": [["steel", "2"]]},
    {"ID": "cosmoteer.structure_1x3_wedge", "Resources": [["steel", "3"]]},
    {"ID": "cosmoteer.structure_tri", "Resources": [["steel", "1"]]},
    {"ID": "cosmoteer.structure_wedge", "Resources": [["steel", "1"]]},
    {"ID": "cosmoteer.thruster_boost","Resources": [["steel", "56"], ["coil2", "10"], ["tristeel", "8"]]},
    {"ID": "cosmoteer.thruster_huge","Resources": [["steel", "80"], ["coil2", "20"], ["tristeel", "10"]]},
    {"ID": "cosmoteer.thruster_large", "Resources": [["steel", "40"], ["coil2", "10"]]},
    {"ID": "cosmoteer.thruster_med", "Resources": [["steel", "24"], ["coil", "9"]]},
    {"ID": "cosmoteer.thruster_small", "Resources": [["steel", "8"], ["coil", "3"]]},
    {"ID": "cosmoteer.thruster_small_2way","Resources": [["steel", "12"], ["coil", "7"]]},
    {"ID": "cosmoteer.thruster_small_3way","Resources": [["steel", "16"], ["coil", "11"]]},
    {"ID": "cosmoteer.tractor_beam_emitter","Resources": [["steel", "200"], ["coil2", "50"], ["diamond", "5"]]},
    {"ID": "he_missiles","Resources": [["missile_part_he", "12"]]},
    {"ID": "nukes","Resources": [["missile_part_nuke", "12"]]},
    {"ID": "mines","Resources": [["mine_part", "24"]]},
    {"ID": "emp_missiles","Resources": [["missile_part_emp", "9"]]},
]

resource_cost = [{'ID': 'bullet', 'BuyPrice': 4, 'MaxStackSize': 20}, {'ID': 'carbon', 'BuyPrice': 160, 'MaxStackSize': 5}, {'ID': 'coil', 'BuyPrice': 100, 'MaxStackSize': 20}, {'ID': 'coil2', 'BuyPrice': 300, 'MaxStackSize': 20}, {'ID': 'copper', 'BuyPrice': 80, 'MaxStackSize': 5}, {'ID': 'diamond', 'BuyPrice': 4000, 'MaxStackSize': 5}, {'ID': 'enriched_uranium', 'BuyPrice': 2000, 'MaxStackSize': 10}, {'ID': 'gold', 'BuyPrice': 500, 'MaxStackSize': 5}, {'ID': 'hyperium', 'BuyPrice': 50, 'MaxStackSize': 20}, {'ID': 'iron', 'BuyPrice': 20, 'MaxStackSize': 5}, {'ID': 'mine_part', 'BuyPrice': 52, 'MaxStackSize': 8}, {'ID': 'missile_part_emp', 'BuyPrice': 20, 'MaxStackSize': 10}, {'ID': 'missile_part_he', 'BuyPrice': 8, 'MaxStackSize': 10}, {'ID': 'missile_part_nuke', 'BuyPrice': 36, 'MaxStackSize': 10}, {'ID': 'processor', 'BuyPrice': 2500, 'MaxStackSize': 5}, {'ID': 'steel', 'BuyPrice': 25, 'MaxStackSize': 20}, {'ID': 'sulfur', 'BuyPrice': 20, 'MaxStackSize': 5}, {'ID': 'tristeel', 'BuyPrice': 200, 'MaxStackSize': 20}, {'ID': 'tritanium', 'BuyPrice': 160, 'MaxStackSize': 5}, {'ID': 'uranium', 'BuyPrice': 400, 'MaxStackSize': 5}]

cat_armor = ["cosmoteer.armor", "cosmoteer.armor_1x2_wedge", "cosmoteer.armor_1x3_wedge", "cosmoteer.armor_2x1", "cosmoteer.armor_structure_hybrid_1x1", "cosmoteer.armor_structure_hybrid_1x2", "cosmoteer.armor_structure_hybrid_1x3", "cosmoteer.armor_structure_hybrid_tri", "cosmoteer.armor_tri", "cosmoteer.armor_wedge", "cosmoteer.structure", "cosmoteer.structure_1x2_wedge", "cosmoteer.structure_1x3_wedge", "cosmoteer.structure_tri", "cosmoteer.structure_wedge"]
cat_crew = ["cosmoteer.crew_quarters_med", "cosmoteer.crew_quarters_small"]
cat_mouvement = ["cosmoteer.engine_room", "cosmoteer.thruster_boost", "cosmoteer.thruster_huge", "cosmoteer.thruster_large", "cosmoteer.thruster_med", "cosmoteer.thruster_small", "cosmoteer.thruster_small_2way", "cosmoteer.thruster_small_3way"]
cat_power = ["cosmoteer.power_storage", "cosmoteer.reactor_large", "cosmoteer.reactor_med", "cosmoteer.reactor_small"]
cat_shield = ["cosmoteer.shield_gen_large", "cosmoteer.shield_gen_small"]
cat_storage = ["cosmoteer.storage_2x2", "cosmoteer.storage_3x2", "cosmoteer.storage_3x3", "cosmoteer.storage_4x3", "cosmoteer.storage_4x4"]
cat_utility = ["cosmoteer.airlock", "cosmoteer.control_room_large", "cosmoteer.control_room_med", "cosmoteer.control_room_small", "cosmoteer.conveyor", "cosmoteer.corridor", "cosmoteer.door", "cosmoteer.explosive_charge", "cosmoteer.factory_ammo", "cosmoteer.factory_coil", "cosmoteer.factory_coil2", "cosmoteer.factory_diamond", "cosmoteer.factory_emp", "cosmoteer.factory_he", "cosmoteer.factory_mine", "cosmoteer.factory_nuke", "cosmoteer.factory_processor", "cosmoteer.factory_steel", "cosmoteer.factory_tristeel", "cosmoteer.factory_uranium", "cosmoteer.fire_extinguisher", "cosmoteer.hyperdrive_beacon", "cosmoteer.hyperdrive_small", "cosmoteer.roof_headlight", "cosmoteer.roof_light", "cosmoteer.sensor_array", "cosmoteer.tractor_beam_emitter"]
cat_weapons = ["cosmoteer.cannon_deck", "cosmoteer.cannon_large", "cosmoteer.cannon_med", "cosmoteer.disruptor", "cosmoteer.flak_cannon_large", "cosmoteer.ion_beam_emitter", "cosmoteer.ion_beam_prism", "cosmoteer.laser_blaster_large", "cosmoteer.laser_blaster_small", "cosmoteer.mining_laser_small", "cosmoteer.missile_launcher", "cosmoteer.point_defense", "cosmoteer.railgun_accelerator", "cosmoteer.railgun_launcher", "cosmoteer.railgun_loader", "he_missiles", "nukes", "mines", "emp_missiles"]


def convert_bytes_to_base64(data):
    if isinstance(data, bytes):
        return base64.b64encode(data).decode('utf-8')
    elif isinstance(data, list):
        return [convert_bytes_to_base64(item) for item in data]
    elif isinstance(data, dict):
        return {key: convert_bytes_to_base64(value) for key, value in data.items()}
    else:
        return data

def price_analysis(data_json): ## take json instead of png
    price_weapons = 0
    price_armor = 0
    price_crew = 0
    price_mouvement = 0
    price_power = 0
    price_shield = 0
    price_storage = 0
    price_utility = 0
    
    data = convert_bytes_to_base64(data_json)
    parts = data["Parts"]
    doors = data["Doors"]
    missile_mapping = {
            0: 'he_missiles',
            1: 'emp_missiles',
            2: 'nukes',
            3: 'mines'
        }
    missile_types = []
    try :
        missile_types = [entry["Value"] for entry in data["PartUIToggleStates"] if entry["Key"][0]["ID"] == "cosmoteer.missile_launcher" and entry["Key"][1] == "DG1pc3NpbGVfdHlwZQ=="]
    except :
        pass
    mapped_output = [] # missile type and number
    for item in missile_types:
        if item in missile_mapping:
            mapped_output.append(missile_mapping[item])
    try:
        storage = data["NewFlexResourceGridTypes"]
    except KeyError:
        storage = None
    total_price = 0
    # calculate price for parts
    for item in parts:
        item_id = item['ID']
        resources = None
        for part in parts_resources:
            if part['ID'] == item_id:
                resources = part['Resources']
                break
        if resources:
            item_price = 0
            for resource in resources:
                resource_id = resource[0]
                resource_quantity = int(resource[1])
                for cost in resource_cost:
                    if cost['ID'] == resource_id:
                        resource_price = cost['BuyPrice']
                        item_price += resource_price * resource_quantity
                        break
            total_price += item_price
            # put price in category
            if item_id in cat_weapons:
                price_weapons += item_price
            elif item_id in cat_armor:
                price_armor += item_price
            elif item_id in cat_crew:
                price_crew += item_price
            elif item_id in cat_mouvement:
                price_mouvement += item_price
            elif item_id in cat_power:
                price_power += item_price
            elif item_id in cat_shield:
                price_shield += item_price
            elif item_id in cat_storage:
                price_storage += item_price
            elif item_id in cat_utility:
                price_utility += item_price
                
                
    # calculate price for missiles
    for item in mapped_output:
        item_id = item
        resources = None
        for part in parts_resources:
            if part['ID'] == item_id:
                resources = part['Resources']
                break
        if resources:
            item_price = 0
            for resource in resources:
                resource_id = resource[0]
                resource_quantity = int(resource[1])
                for cost in resource_cost:
                    if cost['ID'] == resource_id:
                        resource_price = cost['BuyPrice']
                        item_price += resource_price * resource_quantity
                        break
            total_price += item_price
            # add to weapon price
            price_weapons += item_price
    # calculate price for doors
    door_price = 0
    if doors is not None and isinstance(doors, list):
        for door in doors:
            door_id = door['ID']
            for part in parts_resources:
                if part['ID'] == door_id:
                    resources = part['Resources']
                    break
            if resources:
                for resource in resources:
                    resource_id = resource[0]
                    resource_quantity = int(resource[1])
                    for cost in resource_cost:
                        if cost['ID'] == resource_id:
                            resource_price = cost['BuyPrice']
                            door_price += resource_price * resource_quantity
                            break
    # add door price to utility
    price_utility += door_price
    total_price += door_price
    crew_quarters_small_price = 0
    crew_quarters_med_price = 0
    for item in parts:
        item_id = item['ID']
        if item_id == 'cosmoteer.crew_quarters_small':
            crew_quarters_small_price += 1000
        elif item_id == 'cosmoteer.crew_quarters_med':
            crew_quarters_med_price += 3000
    crew = 0
    for item in parts:
        item_id = item['ID']
        if item_id == 'cosmoteer.crew_quarters_small':
            crew += 2
        elif item_id == 'cosmoteer.crew_quarters_med':
            crew += 6
    # add price to crew
    price_crew += crew_quarters_small_price + crew_quarters_med_price
    total_price += crew_quarters_small_price + crew_quarters_med_price
    
    # storage
    storage_price = 0
    if storage is not None:
        for item in storage:
            if 'Value' in item:
                resource_id = item['Value']
                for cost in resource_cost:
                    if cost['ID'] == resource_id:
                        resource_price = cost['BuyPrice']
                        max_stack = cost['MaxStackSize']
                        storage_price += resource_price * max_stack
    # add price to storage
    price_storage += storage_price
    total_price += storage_price
    
    # print("total_price: ", total_price)
    # print("price_crew: ", price_crew)
    # print("price_weapons: ", price_weapons)
    # print("price_armor: ", price_armor)
    # print("price_mouvement: ", price_mouvement)
    # print("price_power: ", price_power)
    # print("price_shield: ", price_shield)
    # print("price_storage: ", price_storage)
    # print("price_utility: ", price_utility)
    

    # Define the categories and values
    categories = ['Shield', 'Weapons', 'Movement', 'Utility', 'Crew', 'Power', 'Armor']
    values = [price_shield, price_weapons, price_mouvement, price_utility, price_crew, price_power, price_armor]

    # Create a blank image
    width, height = 800, 800
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)

    # Center coordinates
    center_x, center_y = width // 2, height // 2

    # Number of categories
    num_categories = len(categories)

    # Calculate the angle between each category
    angle = 360 / num_categories

    # Maximum value for scaling
    max_value = max(values)

    # Radius of the radar chart
    radius = min(center_x, center_y) - 150

    # Draw the radar chart axes
    for i in range(num_categories):
        x1 = center_x + radius * math.cos(math.radians(i * angle))
        y1 = center_y + radius * math.sin(math.radians(i * angle))
        draw.line([(center_x, center_y), (x1, y1)], fill='gray')
        x1 = center_x + radius * math.cos(math.radians(i * angle))
        y1 = center_y + radius * math.sin(math.radians(i * angle))
        x2 = center_x + radius * math.cos(math.radians((i+1) * angle))
        y2 = center_y + radius * math.sin(math.radians((i+1) * angle))
        draw.line([(x1, y1), (x2, y2)], fill='gray')

    # Draw the data points on the radar chart and add labels
    font = ImageFont.load_default()  # You can customize the font as needed

    data_points = []

    for i in range(num_categories):
        normalized_value = values[i] / max_value
        x = center_x + radius * normalized_value * math.cos(math.radians(i * angle))
        y = center_y + radius * normalized_value * math.sin(math.radians(i * angle))
        draw.ellipse([(x - 5, y - 5), (x + 5, y + 5)], fill='blue')
        
        # Add labels
        label_x = center_x + (radius + 20) * math.cos(math.radians(i * angle))
        label_y = center_y + (radius + 20) * math.sin(math.radians(i * angle))
        label = f"{categories[i]}: {values[i]} | {round(values[i] / total_price * 100, 2)}%"
        draw.text((label_x, label_y), label, font=font, fill='black')
        
        # Add the coordinates of the data point to the list
        data_points.append((x, y))
        

    # Draw lines between data points to create a polygon
    draw.polygon(data_points, outline='gray', fill='lightblue')

    # Add label title in the middle top
    title = f"Price Analysis - Total cost : {total_price}"
    title_font = ImageFont.truetype("arial.ttf", 40)  # You can change the font and size as desired
    title_width = draw.textlength(title, font=title_font)
    title_x = center_x - title_width / 2
    title_y = 50  # Adjust the y-coordinate as desired
    draw.text((title_x, title_y), title, font=title_font, fill='black')

    
    # Save or display the radar chart
    # image.show()

    # Create a BytesIO object to hold the image data
    image_data = BytesIO()

    # Save the image to the BytesIO object
    image.save(image_data, format='PNG')

    # Reset the file pointer of the BytesIO object
    image_data.seek(0)

    # Encode the image data as a base64 string
    base64_img = base64.b64encode(image_data.getvalue()).decode('utf-8')


    url_analysis = 'testing'

    # print(base64_img)
    url_analysis = upload_image_to_imgbb(base64_img)
    # print(url_analysis)
    data = {
        "url_analysis": url_analysis,
        "total_price": {"price": total_price, "percent": 1},
        "price_crew": {"price": price_crew, "percent": price_crew / total_price},
        "price_weapons": {"price": price_weapons, "percent": price_weapons / total_price},
        "price_armor": {"price": price_armor, "percent": price_armor / total_price},
        "price_mouvement": {"price": price_mouvement, "percent": price_mouvement / total_price},
        "price_power": {"price": price_power, "percent": price_power / total_price},
        "price_shield": {"price": price_shield, "percent": price_shield / total_price},
        "price_storage": {"price": price_storage, "percent": price_storage / total_price},
    }
    # Convert the dictionary to a JSON string
    json_data = json.dumps(data)
    return json_data 

# for testing
# import cosmoteer_save_tools
# # # data = cosmoteer_save_tools.Ship('https://cdn.discordapp.com/attachments/546321242471530506/1151249538108096652/input_file.png').data
# data = cosmoteer_save_tools.Ship('https://cdn.discordapp.com/attachments/546321242471530506/1151507769317404672/input_file.png').data


# json_data = price_analysis(data)
# print(json_data)