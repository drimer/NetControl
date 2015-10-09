var Device = Backbone.Model.extend({});

var DeviceView = Backbone.View.extend({
    template: _.template(Templates['device_grid_element.html']),

    render: function () {
        var attributes = this.model.toJSON();
        this.$el.html(this.template(attributes));
    }
});

var DeviceCollection = Backbone.Collection.extend({
    model: Device,
    url: '/devices'
});

var DeviceCollectionView = Backbone.View.extend({
    el: '#device-grid',

    initialize: function () {
        this.collection.on('fetch', this.addAll, this);
    },

    addAll: function () {
        this.collection.forEach(this.addDevice, this);
    },

    clean_up: function () {
        this.$el.empty();
    },

    render: function () {
        this.clean_up();
        this.addAll();
    },

    addDevice: function (device) {
        var deviceView = new DeviceView({model: device});
        deviceView.render();
        this.$el.append(deviceView.el);
    }
});

$(document).ready(function () {
    var deviceCollection = new DeviceCollection();
    deviceCollection.fetch().done(function () {
        var deviceCollectionView = new DeviceCollectionView({
            collection: deviceCollection
        });
        deviceCollectionView.render();
    });
});