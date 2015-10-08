var Machine = Backbone.Model.extend({});

var MachineView = Backbone.View.extend({
    template: _.template(Templates['machine_grid_element.html']),

    render: function () {
        var attributes = this.model.toJSON();
        this.$el.html(this.template(attributes));
    }
});

var MachineCollection = Backbone.Collection.extend({
    model: Machine,
    url: '/machines'
});

var MachineCollectionView = Backbone.View.extend({
    el: '#machine-grid',

    initialize: function () {
        this.collection.on('fetch', this.addAll, this);
    },

    addAll: function () {
        this.collection.forEach(this.addMachine, this);
    },

    clean_up: function () {
        this.$el.empty();
    },

    render: function () {
        this.clean_up();
        this.addAll();
    },

    addMachine: function (machine) {
        var machineView = new MachineView({model: machine});
        machineView.render();
        this.$el.append(machineView.el);
    }
});

$(document).ready(function () {
    var machineCollection = new MachineCollection();
    machineCollection.fetch().done(function () {
        var machineCollectionView = new MachineCollectionView({
            collection: machineCollection
        });
        machineCollectionView.render();
    });
});