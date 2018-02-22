struct Example {
    some_int: u32,
    some_string: String,
}

fn test() -> Example {
    Example {
        some_int: 3,
        some_string: String::from("BLA"),
    }
}

fn main()
{
    let Example { ref mut some_string, .. } = test();
    match test() {
        Example { some_int: 3, some_string } =>
            println!("Int was three, string was {}",
                     some_string),
        Example { some_string, .. } =>
            println!("Int was anytthing, string was {}",
                     some_string),
    }
}

