DRApp.me = $.cookie('people-nandy-io-me');

// Persons

DRApp.controller("Person","Base",{
    singular: "person",
    plural: "persons",
    me: function(name) {
        DRApp.me = name;
        $.cookie('people-nandy-io-me', DRApp.me);
        this.application.refresh();
    },
    not_me: function() {
        DRApp.me = '';
        $.cookie('people-nandy-io-me', DRApp.me);
        this.application.refresh();
    }
});

DRApp.template("Persons",DRApp.load("persons"),null,DRApp.partials);

DRApp.route("person_list","/person","Persons","Person","list");
DRApp.route("person_create","/person/create","Create","Person","create");
DRApp.route("person_retrieve","/person/{id:^\\d+$}","Retrieve","Person","retrieve");
DRApp.route("person_update","/person/{id:^\\d+$}/update","Update","Person","update");
