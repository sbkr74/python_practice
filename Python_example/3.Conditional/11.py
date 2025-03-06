# nested-if example

usr_in = int(input("1.Bike\n2.Car\nChoose from above: "))
msg = "No details available."
if usr_in == 1:
    category = int(input("1.Superbike\n2.Sportsbike\n3.Offroads\n4.ATVs\nChoose from above: "))
    if category == 1:
        brands = int(input("1.Kawasaki\n2.Ducati\n3.BMW\n4.KTM\n5.Royal Enfield\nChoose from above: "))
        if brands == 1:
            print("H2R  ->  $80k")
            print("Z1000r-> $37k")
        elif brands == 2:
            print("Panigale v4 ->  $120k")
            print("Monster -> $63k")
        elif brands == 3:
            print("S1000RR ->  $55k")
            print("M1000RR ->  $70k")
        elif brands == 4:
            print("rc 1000 ->  $48k")
            print("Duke 1250-> $47k")
        elif brands == 5:
            print("continental 650 ->$13k")
            print("bullet 500-> $11k")
        else:
            print(msg)
    elif category == 2:
        brands = int(input("1.Suzuki\n2.Yamaha\n3.Honda\n4.TVS\n5.Bajaj\6.Hero\nChoose from above: "))
        if brands == 1:
            print("Hayabusa  ->  $69k")
            print("Gixer 250 -> $11k")
            print("Katana -> 30k")
        elif brands == 2:
            print("R1  ->  $28k")
            print("R15 v4 -> $12k")
            print("MT15  -> $9k")
        elif brands == 3:
            print("CB300R ->  $11k")
            print("Hornet  ->  $8k")
        elif brands == 4:
            print("Apache 310r->  $10")
            print("Raider-> $9k")
        elif brands == 5:
            print("Pulsar 200 ->$8k")
            print("Dominar -> $11k")
        elif brands == 6:
            print("ZXR ->$8k")
            print("Mavrick 440-> $11k")
        else:
            print(msg)
    elif category == 3:
        brands = int(input("1.Ducati\n2.BMW\n3.Hero\nChoose from above: "))
        if brands == 1:
            print("Multistrada  ->  $22k")
            print("DesertX-> $17k")
        elif brands == 2:
            print("R1300 GS ->  $31k")
            print("F900GS   -> $23k")
        elif brands == 3:
            print("impulse ->  $7k")
            print("xpluse -> $8k")
        else:
            print(msg)
    elif category == 4:
        print("ATV -> Staring $13k")
    else:
        print(msg)
elif usr_in == 2:
    print("currently no details available.")
    print("Upcoming brands will be :-\nFerrari\nLamborgini\nRoyals Royce\nLandRover\nand so on...")
    opt = int(input("1.SuperCars\n2.SportsCars\n3.Sedans\n4.SUVs\n5.Offroads\nChoose from above: : "))
else:
    print("Something went wrong.")
